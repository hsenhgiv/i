#HMAC-SHA1 Algorithm 

import hashlib 
import hmac
import base64

print("\n HMAC-SHA1 Algorithm")

def make_digest(message, key):
    
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')
    
    digester = hmac.new(key, message, hashlib.sha1)
    
    signature1 = digester.digest()
    
    signature2 = base64.urlsafe_b64encode(signature1)    
    
    return str(signature2, 'UTF-8')
  
    
Technique = 'HMAC-SHA1'
Text = input("\nEnter the Text : ")
Key = input("\nEnter The Key : ")
E = make_digest(Text, Key)
print ("\nYour Mode      : " + Technique)
print ("\nYour Text      : " + Text)
print ("\nKey            : " + Key)
print ("\nEncrypted Text : " + E)
