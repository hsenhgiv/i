#monoalphabetic cipher
import random
text=input("Enter plain text:-")
alpha = "abcdefghijklmnopqrstuvwxyz"
#Encrypts the plain text message
def encrypt(original, key=None):
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)
        new = []
        for letter in original:
            new.append(key[alpha.index(letter)])
    return ["".join(new), key]


def decrypt(cipher, key=None):
    if key is not None:
        new = []
        for letter in cipher:
            new.append(alpha[key.index(letter)])
    return "".join(new)

if text.isupper():
    ch=text.lower()
else:
    ch=text
e = encrypt(ch, None)
print()
print("Encrypted message and key :-")
print(e) #Prints encrypted message
print()
print("Decrypted message is",decrypt(e[0], e[1])) #Decodes the message and prints it
 
