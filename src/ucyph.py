#!/usr/bin/env python3
# This tool decodes/encodes various ciphers 

import argparse

from ciphers import *

# ---- Function Map ----

FUNCTION_MAP = {'3': caesar,
                '47': rot47,
                '13': rot13,
                '5': vigenere,
                '11': playfair, }


# ---- Function Names ----

def func_names(a):
    FUNCTION_NAMES = {'3': 'Caesar',
                      '13': 'Rot-13',
                      '47': 'Rot-47',
                      '5': 'Vigenere',
                      '11': 'Playfair'}
    return FUNCTION_NAMES[a]


# ---- Arguments ----

parser = argparse.ArgumentParser(description='Encrypt a string.')
parser.add_argument('-c', '--code', required=True, choices=FUNCTION_MAP.keys(), metavar='',
                    help='Encrypt message using the given cipher')
parser.add_argument('-s', '--string', required=True, metavar='', help='String to be Encrypted/Decrypted')
parser.add_argument('-k', '--key', metavar='', help='Key/Password for the cipher')
en_de = parser.add_mutually_exclusive_group()
en_de.add_argument('-D', '--decode', action='store_true', help='decode the string using current cipher')
en_de.add_argument('-E', '--encode', action='store_true', help='encode the string using current cipher')

volume = parser.add_mutually_exclusive_group()
volume.add_argument('-q', '--quiet', action='store_true', help='print quiet')
volume.add_argument('-v', '--verbose', action='store_true', help='print verbose')

args = parser.parse_args()

# ---- Handling ----

if __name__ == '__main__':
    func = FUNCTION_MAP[args.code]

    if args.encode:
        if args.key:
            final = func(args.string, args.key, True)
        else:
            final = func(args.string, True)
    elif args.decode:
        if args.key:
            final = func(args.string, args.key, False)
        else:
            final = func(args.string, False)
    else:
        if args.key:
            final = func(args.string, args.key)
        else:
            final = func(args.string)

    if args.quiet:
        print(final)
    elif args.verbose:
        print(f'Using the {func_names(args.code)} Cipher to encrypt \"{args.string}\" results in:\n\n\"{final}\"')
    else:
        print(f'The encrypted text is: \"{final}\"')
