import rsa

class RSA:
    def __init__(self):
        self.keys = ()
        self.publicKey = []
        self.privateKey = []
        
    def getNewKey(self, bits):
        self.keys = rsa.newkeys(bits)
        self.publicKey = self.keys[0]
        self.privateKey = self.keys[1]
        return self.keys
    
    def getPublicKey(self):
        return "rsa." + str(self.publicKey)
    def getPrivateKey(self):
        return "rsa." + str(self.privateKey)
    
    def selectPublicKey(self, key):
        self.publicKey = eval(key)
    def selectPrivateKey(self, key):
        self.privateKey = eval(key)

    def encrypt(self, message):
        message = message.encode("utf-8")
        
        self.EncryptedMessage = str(rsa.encrypt(message, self.publicKey))[2:-1]
        
        return self.EncryptedMessage
    def decrypt(self, message):
        message = bytes(message,'ISO-8859-1').decode('unicode_escape').encode('ISO-8859-1')
        self.DecryptedMessage = rsa.decrypt(message, self.privateKey)
        return str(self.DecryptedMessage)[2:-1]
    
