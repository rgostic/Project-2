
from ciphers import Cipher
from caesar import *
from polybius import *
from affine import *


def getCypherDecision():
	return input('What cypher would you like to use\n(1) Caesar\n(2) Polybius\n(3) Affine\n')

def getUnencryptedString():
	return input('Please type the message you want to encrypt:\n')

def getEncryptedString():
	return input('Please type the code you want to decrypt:\n')

def processCypherEncryption(decision, unencodedString):
	if (decision == "1"):
		c = Caesar()
		return c.encrypt(unencodedString)		

	if (decision == "2"):
		c = Polybius()
		return c.encrypt(unencodedString)		
	
	if (decision == "3"):
		c = Affine()
		return c.encrypt(unencodedString)
		
def processCypherDecryption(decision, encodedString):
	if (decision == "1"):
		c = Caesar()
		return c.decrypt(encodedString)		

	if (decision == "2"):
		c = Polybius()
		return c.decrypt(encodedString)		
	
	if (decision == "3"):
		c = Affine()
		return c.decrypt(encodedString)


def getEncryptDecision(encryptDecision):
	
	if decision.lower() == 'e':

		cypherDecision = getCypherDecision()
		unencodedString = getUnencryptedString()
		return processCypherEncryption(cypherDecision, unencodedString)
		

	elif decision.lower() == 'd':

		cypherDecision = getCypherDecision()
		encodedString = getEncryptedString()	
		return processCypherDecryption(cypherDecision, encodedString)
		
def validDecision(decision):
	if (decision.lower() == 'e' or decision.lower() == 'd'):
		return True
	else:
		return False

decision = input('Would you like to (e) Encrypt or (d) Decrypt a message?\n').lower()
while (validDecision(decision) != True):
	decision = input('Please enter a valid selection...\n''Would you like to (e) Encrypt or (d) Decrypt a message?\n')

print("result: " + getEncryptDecision(decision))


