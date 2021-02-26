import sys 

def encrypt(message, key):
    final = ""
    
    for i in range(len(message)):
        temp = 0
        if ' ' in message[i]:
            final += ' '
            continue
        
        if message[i].isupper():
            temp = (ord(message[i]) - 65 + key)%26 + 65
            final += chr(temp)
        else:
            temp = (ord(message[i]) - 97 + key)%26 + 97
            final += chr(temp)
    return final

def decrypt(message, key):
    final = "" 

    for i in range(len(message)):
        temp = 0
        if ' ' in message[i]:
            final += ' '
            continue

        if message[i].isupper():
            temp = (ord(message[i]) - 65 - key) % 26 + 65
            final += chr(temp)
        else:
            temp = (ord(message[i]) - 97 - key) % 26 + 97
            final += chr(temp)
    return final

message = input("What is your message? ")
key = int(input("What is your key (number)? "))
choose = input("Do you want to encrypt or decrypt? ")

if choose == "encrypt":
    encrypted = encrypt(message, key)
    print(message, "encrypted is", encrypted, "with a key of", key)
else:
    decrypted = decrypt(message, key)
    print(message, "decrypted is", decrypted, "with a key of", key)


   

