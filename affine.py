import string

from ciphers import Cipher


class Affine(Cipher):
    FORWARD = string.ascii_uppercase * 3
    MAP = {}
    forcedMAP = {}
    
    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase
        for i in range(26):
            self.MAP[chr(i+65).lower()] = chr(((5*i+8)%26)+65).lower()
            self.forcedMAP[chr(((5*i+8)%26)+65).lower()] = chr(i+65).lower()

    def encrypt(self, text):
        output = []

        for char in text:
            if char in self.MAP.keys():
                output.append(self.MAP[char])

        return ''.join(output)

    def decrypt(self, text):
        output = []
        for char in text:
            if char in self.forcedMAP.keys():
                output.append(self.forcedMAP[char])
        return ''.join(output)