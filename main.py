
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
        elif message[i].islower():
            temp = (ord(message[i]) - 97 + key)%26 + 97
            final += chr(temp)
        else:
            final += message[i]
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
        elif message[i].islower():
            temp = (ord(message[i]) - 97 - key) % 26 + 97
            final += chr(temp)
        else:
            final += message[i]
        
    return final

def main():
    files = input("What file would you like to encrypt or decrypt? ")
    
    choose = input("Do you want to encrypt or decrypt? ")
    if choose != "encrypt" and choose != "decrypt": 
        print("not valid")
        return
    key = int(input("What is your key (number)? "))
    if type(key) != int:
        print("not valid")
        return

    message = open(files, "r")
    
    if choose == "encrypt":
        encrypted = encrypt(message.read(), key)
        print("Your file has been encrypted and is labeled encrypted.txt")
        f = open("encrypted.txt", "w")
        f.write(encrypted)
        f.close()

    else:
        decrypted = decrypt(message.read(), key)
        print("Your file has been decrypted and is labeled decrypted.txt")
        f = open("decrypted.txt", "w")
        f.write(decrypted)
        f.close()
    
    message.close()

main() 



   

