
# This tool decodes/encodes various ciphers 

import argparse


# ---- Ciphers ----

# OG Caesar - shift of 3 
def caesar(strng, encode=True):
    az = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    if encode:
        for i in strng:
            if i.isalpha():
                 new += az[(az.index(i) + 3) % 26]
            else:
                new += i
    else:
        for i in strng:
            if i.isalpha():
                if az.index(i) < 3:
                     new += az[26 - (abs(az.index(i) - 3) % 26)]
                else:
                    new += az[az.index(i) - 3]
            else:
                new += i
    return new


# ROT-47
def rot47(strng):
    key = '!"#$%&' + "'" + '()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    words = strng.split(' ')
    final = []

    for word in words:
        crypted = []
        for letter in word:
            crypted.append(key[(key.index(letter) + 47) % 94])
        final.append(''.join(crypted))

    return ' '.join(final)


# ROT-13
def rot13(strng):
    az = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for i in strng:
        if i.isalpha():
            if i.islower():
                if az.index(i) < 13:
                    decrypted += az[az.index(i) + 13]
                elif az.index(i) >= 13:
                    decrypted += (az[(az.index(i) + 13) % 13])
            else:
                if az.upper().index(i) < 13:
                    decrypted += az.upper()[az.upper().index(i) + 13]
                elif az.upper().index(i) >= 13:
                    decrypted += az.upper()[(az.upper().index(i) + 13) % 13]
        else:
            decrypted += i
    return decrypted


# ---- Function Map ----

FUNCTION_MAP = {'3':caesar,
                '47':rot47,
                '13':rot13}



# ---- Function Names ----
def func_names(a):
    FUNCTION_NAMES = {'3':'Caesar',
                      '13':'Rot-13',
                      '47':'Rot-47',}
    return FUNCTION_NAMES[a]

# ---- Handling ----

parser = argparse.ArgumentParser(description='Encrypt a string.')
parser.add_argument('-c','--code', required=True, choices=FUNCTION_MAP.keys(), metavar='', help='Encrypt message using the given cipher')
parser.add_argument('-s','--string', required=True, metavar='', help='String to be Encrypted/Decrypted')

en_de = parser.add_mutually_exclusive_group()
en_de.add_argument('-D', '--decode', action='store_true', help='decode the string using current cipher')
en_de.add_argument('-E', '--encode', action='store_true', help='encode the string using current cipher')

volume = parser.add_mutually_exclusive_group()
volume.add_argument('-q','--quiet', action='store_true', help='print quiet')
volume.add_argument('-v','--verbose', action='store_true', help='print verbose')

args = parser.parse_args()


if __name__ == '__main__':
    func = FUNCTION_MAP[args.code]

    if args.encode:
        final = func(args.string, True)
    elif args.decode:
        final = func(args.string, False)
    else:
        final = func(args.string)

    if args.quiet:
        print(final)
    elif args.verbose:
        print(f'Using the {func_names(args.code)} Cipher to encrypt \"{args.string}\" results in:\n\n\"{final}\"')
    else:
        print(f'The encrypted text is: \"{final}\"')




