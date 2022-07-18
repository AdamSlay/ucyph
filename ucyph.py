
# This tool decodes/encodes various ciphers 

import argparse



# ---- Ciphers ----

# OG Caesar 
def caesar(strng):
    az = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    for i in strng:
        new += az[(az.index(i) + 3) % 26]
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

FUNCTION_MAP = {'caesar':caesar,
                'rot47':rot47,
                'rot13':rot13}


# ---- Handling ----

parser = argparse.ArgumentParser(description='En/De-crypt a string.')
parser.add_argument('command', choices=FUNCTION_MAP.keys(), help='Encrypt message using the given cipher')
parser.add_argument('string', help='String to be En/De-crypted')
args = parser.parse_args()
func = FUNCTION_MAP[args.command]
print(func(args.string))
