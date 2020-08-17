import importlib

rsa = importlib.import_module("RSA")

RSA_instance = rsa.RSA()

def help():
    print("get_new_key \ndecrypt \nencrypt \nselectPublicKey \nselectPrivateKey \ngetPublicKey \ngetPrivateKey")    


while(True):
    command = input("Command > ")    
    
    if command == "get_new_key":
        keys = RSA_instance.get_new_key()
        print("\nPublicKey: rsa." + str(keys[0]) + "\n")
        print("PrivateKey: rsa." + str(keys[1]) +"\n")
    elif command == "decrypt":
        print(RSA_instance.decrypt())
    elif command == "encrypt":
        print(RSA_instance.encrypt())
    elif command == "getPublicKey":
        print(RSA_instance.getPublicKey())
    elif command == "getPrivateKey":
        print(RSA_instance.getPrivateKey())
    elif command == "selectPublicKey":
        RSA_instance.selectPublicKey()
        if input("do you want to encrypt ? (Y/N): ").capitalize() == "Y":
            print(RSA_instance.encrypt())
    elif command == "selectPrivateKey":
        RSA_instance.selectPrivateKey()
        if input("do you want to decrypt ? (Y/N): ").capitalize() == "Y":
            print(RSA_instance.decrypt())
            
    elif command == "help":
        help()
    else:
        print("wrong command, use \'help\' to get a list of all commands.")
