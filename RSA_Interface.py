import importlib

RSA = importlib.import_module("RSA")

def help():
    print("getNewKey \ndecrypt \nencrypt \nselectPublicKey \nselectPrivateKey \ngetPublicKey \ngetPrivateKey")    

def getNewKey(bits):
    keys = RSA.getNewKey(bits)
    print("\nPublicKey: rsa." + str(keys[0]) + "\n")
    print("PrivateKey: rsa." + str(keys[1]) +"\n")

getNewKey(1024)

while(True):
    command = input("Command > ")    
    
    if command == "getNewKey":
        bits = int(input("how many bits ? "))
        getNewKey(bits)
    elif command == "decrypt":
        message = input("enter your encrypted message: ")
        print(RSA.decrypt(message))
        
    elif command == "encrypt":
        message = input("enter your message: ")
        print(RSA.encrypt(message))
        
    elif command == "getPublicKey":
        print(RSA.getPublicKey())
        
    elif command == "getPrivateKey":
        print(RSA.getPrivateKey())
        
    elif command == "selectPublicKey":
        key = input("enter your PublicKey (rsa.PublicKey(....)): ")
        RSA.selectPublicKey(key)
        if input("do you want to encrypt ? (Y/N): ").capitalize() == "Y":
            message = input("enter your message: ")
            print(RSA.encrypt(message))
        
    elif command == "selectPrivateKey":
        key = input("enter your PrivateKey (rsa.PrivateKey(....)): ")
        RSA.selectPrivateKey(key)
        if input("do you want to decrypt ? (Y/N): ").capitalize() == "Y":
            message = input("enter your encrypted message: ")
            print(RSA.decrypt(message))
            
    elif command == "help":
        help()
  
    else:
        print("wrong command, use \'help\' to get a list of all commands.")
