#!/usr/bin/env python3

import argparse

from src.ucyph import __version__ as version
from src.ucyph.ciphers import *
from src.ucyph.utils import read_file, write_file

FUNCTION_MAP = {'3': caesar,
                '47': rot47,
                '13': rot13,
                '5': vigenere,
                '11': playfair, }


def func_names(a):
    """
    Return the name of the cipher function
    :param a: The usage code of the cipher
    :return: The name of the cipher function
    """
    FUNCTION_NAMES = {'3': 'Caesar',
                      '13': 'Rot-13',
                      '47': 'Rot-47',
                      '5': 'Vigenere',
                      '11': 'Playfair'}
    return FUNCTION_NAMES[a]


def parse_args():
    """
    Parse the command line arguments
    :return: The parsed arguments
    """
    ciphers = """
    Cipher list and usage codes:
    | Cipher   | Usage Code  | Requires Key |
    |----------|-------------|--------------|
    | Caesar   | 3           | No           |
    | Vigenere | 5           | Yes          |
    | Playfair | 11          | Yes          |
    | Rot-13   | 13          | No           |
    | Rot-47   | 47          | No           |
    """
    parser = argparse.ArgumentParser(description='Encrypt a file using historical ciphers', epilog=ciphers, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {version}')
    parser.add_argument('code', choices=FUNCTION_MAP.keys(), metavar='', help='usage code for the cipher being used')
    parser.add_argument('file', metavar='', help='file to be encrypted/decrypted')
    parser.add_argument('-o', '--output', metavar='', help='output file')
    parser.add_argument('-k', '--key', metavar='', help='key/password for the cipher')

    en_de = parser.add_mutually_exclusive_group()
    en_de.add_argument('-d', '--decode', action='store_true', help='decode the string using current cipher')
    en_de.add_argument('-e', '--encode', action='store_true', help='encode the string using current cipher')

    return parser.parse_args()


def main():
    try:
        args = parse_args()
        func = FUNCTION_MAP[args.code]
        encode = args.encode if args.encode or args.decode else True

        if args.code in ['5', '11'] and args.key is None:
            raise argparse.ArgumentError(None,
                                         f"The -k/--key argument is required for the selected cipher: {func_names(args.code)}"
                                         f"\n\nUsage: ucyph {args.code} {args.file} -k <key> [-o <output_file>] [-d/-e]")

        text = read_file(args.file)
        final = func(text, args.key, encode) if args.key else func(text, encode)

        out_file = args.output if args.output else args.file
        write_file(final, out_file)

        crypt = 'decrypted' if args.decode else 'encrypted'
        print(f'The {crypt} text has been saved to \"{out_file}\"')

    except FileNotFoundError as e:
        print(f'Error reading from input file: {e}')
    except PermissionError as e:
        print(f'Permission denied: {e}')
    except argparse.ArgumentError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
    main()
