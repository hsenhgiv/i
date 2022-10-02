#Caesar Cipher Technique

print ("\nCaesar Cipher Technique")

def encrypt(text,s):
    result = ("")
 

    for i in range(len(text)):   
        char = text[i]   
 
        
        if (char.isupper()): 
            
            result += chr((ord(char) + Shift - 65) % 26 + 65) 
            
            
 
        
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)
            

    return result


#check the above function

Technique = input("\nEnter the Caesar Cipher Technique, \ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n")

if Technique =='Encrypt':
    Text = input("\nEnter the Plain Text : ")
    Shift = int(input("\nEnter Key : "))
    E = encrypt(Text,Shift)
    print ("\nYour Text      : " + Text)
    print ("\nShift          : " + str(Shift))
    print ("\nEncrypted Text : " + E)
    
elif Technique =='Decrypt':
    Text = input("\nEnter the Cipher Text : ")
    Shift = int(input("\nEnter the key : "))
    D = encrypt(Text,(26 - Shift))
    print ("\nYour Cipher Text    : " + Text)
    print ("\nShift               : " + str(Shift))
    print ("\nDecrypted Text      : " + D)
    
else :
    print ("Wrong Choice Please Try Again ... ")
