import importlib

rsa = importlib.import_module("RSA")

RSA_instance = rsa.RSA()

def help():
    print("getNewKey \ndecrypt \nencrypt \nselectPublicKey \nselectPrivateKey \ngetPublicKey \ngetPrivateKey")    


while(True):
    command = input("Command > ")    
    
    if command == "getNewKey":
        bits = int(input("how many bits ? "))
        keys = RSA_instance.getNewKey(bits)
        print("\nPublicKey: rsa." + str(keys[0]) + "\n")
        print("PrivateKey: rsa." + str(keys[1]) +"\n")
        
    elif command == "decrypt":
        message = input("enter your encrypted message: ")
        print(RSA_instance.decrypt(message))
        
    elif command == "encrypt":
        message = input("enter your message: ")
        print(RSA_instance.encrypt(message))
        
    elif command == "getPublicKey":
        print(RSA_instance.getPublicKey())
        
    elif command == "getPrivateKey":
        print(RSA_instance.getPrivateKey())
        
    elif command == "selectPublicKey":
        key = input("enter your PublicKey (rsa.PublicKey(....)): ")
        RSA_instance.selectPublicKey(key)
        if input("do you want to encrypt ? (Y/N): ").capitalize() == "Y":
            message = input("enter your message: ")
            print(RSA_instance.encrypt(message))
        
    elif command == "selectPrivateKey":
        key = input("enter your PrivateKey (rsa.PrivateKey(....)): ")
        RSA_instance.selectPrivateKey(key)
        if input("do you want to decrypt ? (Y/N): ").capitalize() == "Y":
            message = input("enter your encrypted message: ")
            print(RSA_instance.decrypt(message))
            
    elif command == "help":
        help()
    else:
        print("wrong command, use \'help\' to get a list of all commands.")
