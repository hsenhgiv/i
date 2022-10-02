# Diffie-Hellman Key Agreement Algorithm.

from __future__ import print_function

print("\nDiffie-Hellman Key Agreement Algorithm.\n")


print("\nAlice is a Person A.")
print("\n& Bob is a Person B.")

print("\nAlice & Bob both can Have Publicly Shared Variables.")

print("\n-------------------------------------------------------\n")

p = int(input("\nEnter the Value for Shared Prime 'p'   : \t"))
print("")

g = int(input("\nEnter the Value for Shared Base 'g'    : \t"))
print("")

a = int(input("\nEnter the Value of Secret for Alice 'a': \t"))
print("")

b = int(input("\nEnter the Value of Secret for Bob 'b'  : \t"))
print("")

print("\n-------------------------------------------------------\n")
 
 
# Variables Used
sharedPrime = p    # p
sharedBase = g      # g
 
aliceSecret = a     # a
bobSecret = b      # b
 
# Begin

print("\n\tPublicly Shared Prime            : " , sharedPrime)
print("\n\tPublicly Shared Base             : " , sharedBase)

print("\n-------------------------------------------------------\n")

# Alice Sends Bob A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print("\n\tAlice Sends Over Public Channel  : " , A)
 
# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print("\n\tBob Sends Over Public Channel    : " , B)

print("\n-------------------------------------------------------\n")

print("\nAlice & Bob both Had Privately Calculated their Shared Secret : ")

# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("\n\tAlice Shared Secret              : ", aliceSharedSecret)
 
# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print("\n\tBob Shared Secret                : ", bobSharedSecret)


print("\n-------------------------------------------------------\n")
