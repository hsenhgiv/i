#RSA Algorithm

print ("\nRSA Algorithm")

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('\nNo modular multiplicative inverse for block ' + str(m) + '.\n')
    return c

def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('\nNo modular multiplicative inverse for block ' + str(c) + '.\n')
    return m

def encrypt_string(s):
    ''.join(str(chr(encrypt_block(ord(x)))) for x in s)
    return ''.join(str(chr(encrypt_block(ord(x)))) for x in s)

def decrypt_string(s):
    ''.join(str(chr(decrypt_block(ord(x)))) for x in s)
    return ''.join(str(chr(decrypt_block(ord(x)))) for x in s)

def Testing(Text,E):
    
    Test = input("\nDo you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")

    if Test == 'Yes':
        Technique = 'Decrypt'
        myMessage = E
        Text = myMessage
        D = decrypt_string(Text)
        print ("\n\nYour Mode         : " + Technique)
        print ("\nP                   : " + str(p))
        print ("\nQ                   : " + str(q))
        print ("\nphi(n)              : " + str(phi))
        print ("\nPublic Key          : " + "e = " + str(e) + ", n = " + str(n))
        print ("\nPrivate Key         : " + "d = " + str(d) + ", n = " + str(n))
        print ("\nYour Encrypted Text : " + Text)
        print ("\nDecrypted Text      : " + D + "\n")

    elif Test == 'No':
        print ("\nThank You...!\n")

    else:
        print ("\nPlease Try Again...!\n")
        Testing(Text,E)
    
#check the above function

print("\nThe general formula for Euler's totient function is :\n")
print("\nIF [p ≥ 1 and q ≥ 1] AND [gcd(p, q) = 1] THEN 'φ(p × q) = φ(p) × φ(q)'\n")

Technique = input("\n\nEnter Your Choice for RSA Algorithm, \n\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n")
try:
    input = raw_input
except NameError:
    pass

try:
    chr = unichr
except NameError:
    pass

p = int(input("\nEnter the Value for Prime 'p': \t"))
print("")

q = int(input("\nEnter the Value for Prime 'q': \t"))
print("")

print("\nGiven primes :\tp = " + str(p) + ",\tq = " + str(q)+ ".")

n = p * q
print("\nn = p * q = " + str(n) + "\n")

phi = (p-1)*(q-1)
print("\nEuler's function (totient) [phi(n)]: " + str(phi) + ".")

print("\nThis is List of Co-Primes Arrays for given Prime Numbers:\n")
print(str(coprimes(phi)) + "\n")

e = int(input("\nChoose an Value for 'e' or 'co-prime' from a above Co-Primes Array :\t"))
d = modinv(e,phi)

print("\nYour public key is a pair of numbers ( e = " + str(e) + ", n = " + str(n) + ").")
print("\nYour private key is a pair of numbers (d = " + str(d) + ", n = " + str(n) + ").")

if Technique =='Encrypt':
    Text = input("\nEnter the Number You want to be Converted...\n\n")
    E = encrypt_string(Text)
    print ("\n\nYour Mode         : " + Technique)
    print ("\nP                   : " + str(p))
    print ("\nQ                   : " + str(q))
    print ("\nphi(n)              : " + str(phi))
    print ("\nPublic Key          : " + "e = " + str(e) + ", n = " + str(n))
    print ("\nPrivate Key         : " + "d = " + str(d) + ", n = " + str(n))
    print ("\nYour Number Text    : " + Text)
    print ("\nEncrypted Text      : " + E + "\n")
    Testing(Text,E)
    
    
elif Technique =='Decrypt':
    Text = input("\nEnter the Cipher Text You want to be Decrypted...\n\n")
    D = decrypt_string(Text)
    print ("\n\nYour Mode         : " + Technique)
    print ("\nP                   : " + str(p))
    print ("\nQ                   : " + str(q))
    print ("\nphi(n)              : " + str(phi))
    print ("\nPublic Key          : " + "e = " + str(e) + ", n = " + str(n))
    print ("\nPrivate Key         : " + "d = " + str(d) + ", n = " + str(n))
    print ("\nYour Encrypted Text : " + Text)
    print ("\nDecrypted Text      : " + D + "\n")
    
else :
    print ("Wrong Choice Please Try Again ... ")

