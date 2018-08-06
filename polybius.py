import string

from ciphers import Cipher


class Polybius(Cipher):
    FORWARD = string.ascii_uppercase * 3
    MAP = {}
    reverseMAP = {}


    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase
        for i in range(1,6):
            for j in range(1, 6):
                self.MAP[chr(97 - 1 + (i - 1) * 5 + j)] = str(i) + str(j)
                self.reverseMAP[str(i) + str(j)] = chr(97 - 1 + (i - 1) * 5 + j)
        self.MAP['z'] = str(66)





    def encrypt(self, text):
        output = []
        
        for char in text.lower():            
            if char in self.MAP.keys():
                output.append(self.MAP[char])

        return ' '.join(output)

    def decrypt(self, text):
        output = []
        encodedMessage = text.split(' ')
        
        for eChar in encodedMessage:
            if eChar in self.reverseMAP.keys():
                output.append(self.reverseMAP[eChar])

        return ''.join(output)