#A python program to illustrate Vernam Cipher Technique.

print ("#A python program to illustrate Vernam Cipher Technique.")

def Encrypt(message,key):
    message=str(message)
    m=message.upper().replace("","")#Convert to upper case
    encrypt=""
    #if the key value is not a number,then run with kry=0
    for i in range(len(m)):
        letter=ord(m[i])-65#Letter now range 0-25
        s=key.upper().replace("","")
        l=ord(s[i])-65
        #print("\n",l)
        letter=(letter+l)#Alpha numeric+key mod25=0-25
        #print(letter)
        if letter>25:
            letter=letter-26
            letter+=65
        else:
            #letter=letter
            letter+=65
        encrypt+=chr(letter)#Concatenate message
    return encrypt
def Decrypt(message,key):
    message=str(message)
    m=message.upper().replace("","")#Convert to upper case
    decrypt=""
    #if the key value is not a number,then run with kry=0
    for i in range(len(m)):
        le=ord(m[i])-65#Letter now range 0-25
        s=key.upper().replace("","")
        letter=ord(s[i])-65
        le=le-letter#Alpha numeric+key mod25=0-25
        if le<0:
            le=(le+26)
            le+=65
            
        else:
            le+=65
        decrypt+=chr(le)#Concatenate message
    return decrypt
def Testing(Text,Key,E):
    
    Test = input("Do you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")

    if Test == 'Yes':
        Technique = 'Decrypt'
        myKey = Key
        Key = myKey
        myMessage = E
        Text = myMessage
        D = Decrypt(Text, Key)
        print ("Your Mode        : " + Technique)
        print ("Your Cipher Text : " + Text)
        print ("Key              : " + Key)
        print ("Decrypted Text   : " + D)

    elif Test == 'No':
        print ("Thank You...!\n")

    else:
        print ("Please Try Again...!\n")
        
Technique = input("Enter Your Choice for Vernam Cipher Technique, i.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n")

if Technique =='Encrypt':
    Text = input("Enter the Text You want to be Converted...\n\n")
    Key = input("Enter The Key of your Choice\n\n")
    E = Encrypt(Text,Key)
    print ("Your Mode      : " + Technique)
    print ("Your Text      : " + Text)
    print ("Key            : " + Key)
    print ("Encrypted Text : " + E)
    Testing(Text,Key,E)
elif Technique =='Decrypt':
    Text = input("Enter the Vernam Cipher Text You want to be Decrypted...\n\n")
    Key = input("Enter the Key provided to You...\n\n")
    D = Decrypt(Text,Key)
    print ("Your Mode                  : " + Technique)
    print ("Your Vernam Cipher Text    : " + Text)
    print ("Key                        : " + Key)
    print ("Decrypted Text             : " + D)
    
else :
    print ("Wrong Choice Please Try Again ... ")
