import rsa

class RSA:
    def __init__(self):
        self.keys = ()
        self.publicKey = []
        self.privateKey = []
    def get_new_key(self):
        self.bits = int(input("how many bits ? "))
        self.keys = rsa.newkeys(self.bits)
        self.publicKey = self.keys[0]
        self.privateKey = self.keys[1]
        return self.keys
    
    def getPublicKey(self):
        return "rsa." + str(self.publicKey)
    def getPrivateKey(self):
        return "rsa." + str(self.privateKey)
    
    def selectPublicKey(self):
        self.key = input("enter your PublicKey (rsa.PublicKey(....)): ")
        self.publicKey = eval(self.key)
    def selectPrivateKey(self):
        self.key = input("enter your PrivateKey (rsa.PrivateKey(....)): ")
        self.privateKey = eval(self.key)

    def encrypt(self):
        self.message = input("enter your message: ")
        
        self.message = self.message.encode("utf-8")
        
        self.EncryptedMessage = str(rsa.encrypt(self.message, self.publicKey))[2:-1]
        
        return self.EncryptedMessage
    
    def decrypt(self):
        self.message = bytes(input("enter your encrypted message: "),'ISO-8859-1').decode('unicode_escape').encode('ISO-8859-1')
        self.DecryptedMessage = rsa.decrypt(self.message, self.privateKey)
        return str(self.DecryptedMessage)[2:-1]
    
