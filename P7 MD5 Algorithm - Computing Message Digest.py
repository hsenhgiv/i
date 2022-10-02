#MD5 Algorithm .

import hashlib 
  
print("\nMD5 Algorithm\n")


Text = input("\nEnter the Text: ")
print("\n-------------------------------------------------------\n")

result = hashlib.md5(Text.encode()) 
  

print("\nYour Text : ", Text) 
print("\nThe byte equivalent of hash is : ") 
print(result.digest())


print("\n-------------------------------------------------------\n")
print("\nYour Text : ", Text)
print("\nThe hexadecimal equivalent of hash is : \n") 
print(result.hexdigest()) 
