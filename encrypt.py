from pathlib import Path
import os

"program to encrypt the text of a given file or take user input text and encrypt it using chosen algorithm(s)"
"saves encrypted text to file specified by user"


def caesar(plaintext, shift):
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) == 10:
            ciphertext += "\n"
        elif ord(plaintext[i]) + shift > 126:
            ciphertext += chr(((ord(plaintext[i]) + shift) % 126) + 31)
        else:
            ciphertext += chr(ord(plaintext[i]) + shift)
    return ciphertext

def xor(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key))
    return ciphertext

def backshift(plaintext,shift):
    '''shifts each ASCII character to the left 'shift' number of times .
    wraps around if this is below the range of printable characters.'''
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) == 10:
            ciphertext += "\n"
        elif (ord(plaintext[i]) - shift) < 32:
            ciphertext += chr(126 - (shift - (ord(plaintext[i]) - 31)))
        else:
            ciphertext += chr(ord(plaintext[i]) - shift)
    return ciphertext

def rot13(plaintext):
    '''performs the ROT13 encryption algorithm on the given plaintext.
    Wraps around to beginning of printable ASCII characters if go beyond the printable range'''
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) == 10:
            ciphertext += "\n"
        elif ord(plaintext[i]) + 13 > 126:
            ciphertext += chr(((ord(plaintext[i]) + 13) % 126) + 31)
        else:
            ciphertext += chr(ord(plaintext[i]) + 13)
    return ciphertext

def vigenere(plaintext, keyword):
    "encrypts the plaintext using the Vigenere cipher and given keyword"
    ciphertext = ""
    "modifying the keyword to match the length of the ciphertext"
    index = 0
    while not (len(keyword) == len(plaintext)):
        if len(keyword) > len(plaintext):
            while len(keyword) > len(plaintext):
                keyword = keyword[:-1]
                if len(keyword) == len(plaintext):
                    break
        else:
            keyword += keyword[index]
            index += 1
    for i in range(len(plaintext)):
        if ord(plaintext[i]) == 10:
            ciphertext += "\n"
            continue
        col = ord(plaintext[i]) - 32
        offset = ord(keyword[i]) - 32
        if (col + offset) > 126:
            ciphertext += chr(((col + offset) % 126) + 31)
        else:
            ciphertext += chr((col + offset))
    return ciphertext

def algorithms():
    "prints the 4 different algorithms"
    print("These are the algorithms you can use to encrypt the text: \n1. Caesar Cipher\n2. Backshift Cipher\n3. ROT13 Cipher\n4. Vigenere Cipher\nEnter 'h' for more information on each algorithm.")
    return

def algorithmsInfo():
    "prints info on the 4 encryption algorithms"
    print("1. Caesar Cipher: Each ASCII character in the text is shifted forward by a number of your choosing.\n2. Backshift Cipher: Each ASCII character in the text is shifted backwards by a number of your choosing.\n3. ROT13 Cipher: Each ASCII character is shifted specifically 13 times forward.\n4. Vigenere Cipher: Each ASCII character is mapped to a table of characters based on a 3-letter keyword of your choosing.")
    return 

def texttofile(filename, txt):
    "creates or opens the file called 'filename' and writes the txt to it"
    file = open(filename, "w")
    file.write(txt)
    return

def validInt(string):
    "checks if a string is of a 1- or 2-digit integer in range [0,95]"
    if len(string) not in range(1,3):
        return False
    for i in string:
        if ord(i) not in range(48,58):
            return False
    if int(string) not in range(0,96):
        return False
    return True

def validKey(string):
    "checks if a string is of a single alphabetical letter"
    if not(len(string) == 1):
        return False
    if (not(ord(string[0]) in range(97,123))) and (not(ord(string[0]) in range(65,91))):
        return False
    return True

def validKeyword(string):
    "checks if a string is a 3-letter string"
    "MAKE SURE IT'S ALL LOWERCASE PLS FOR THE LOVE OF GOD I CAN'T DEBUG THIS"
    if not(len(string) == 3):
        return False
    '''if string[0].islower():
        if (not string[1].isupper()) or (not string[2].isupper()):
            return False
    else:
        if (not string[1].islower()) or (not string[2].islower()):
            return False'''
    for char in string:
        if not(char.islower()):
            return False
        if (not(ord(char) in range(97,123))):
            return False
    return True


while(True):
    inputType = input("Enter 1 to encrypt an existing text file or 2 to type something to encrypt: ")
    while inputType not in ["1", "2"]:
        inputType = input("Invalid input, please try again. Enter 1 to encrypt an existing text file or 2 to type something to encrypt: ")
    if inputType == "1":
        inputFileName = input("Enter the name of the file you want to encrypt: ")
        path = Path(inputFileName)
        while not path.is_file():
            print("File","'",inputFileName,"'","not found.")
            inputFileName = input("Enter the name of the file you want to encrypt: ")
            path = Path(inputFileName)
            if path.is_file():
                break
        
        if os.path.getsize(inputFileName) == 0:
            print("File '",inputFileName,"' empty.")
            break
        inputFile = open(inputFileName, "r")
        inputText = inputFile.read()
        inputFile.close()
    else:
        "create a file to write to"
        createFile = input("Enter the name of the file you want to write your text to: ")
        while len(createFile) == 0:
            createFile = input("Invalid input, please try again. Enter the name of the file you want to write your text to: ")
        inputText = input("Enter the text you want to encrypt: ")
        texttofile(createFile, inputText)



    outputName = input("Enter the name of the file you want to save the encrypted text to: ")
    while len(outputName) == 0:
        outputName = input("Invalid input, please try again. Enter the name of the file you want to save the encrypted text to: ")
    outputFile = open(outputName, "w")

    print("There are three levels of encryption: 1, 2, and 3")
    numLevels = input("Enter the number of levels you want to encrypt the text to: ")
    while numLevels not in ["1", "2", "3"]:
        numLevels = input("Invalid input, please try again. Enter the number of levels you want to encrypt the text to: ")

    levels = []

    algorithms()

    decryptionKey = ""

    for i in range(int(numLevels)):
        print("For level",i+1,":")
        algorithm = input(" Enter the number of the algorithm you want to use: ")
        while algorithm == "h":
            algorithmsInfo()
            print("For level",i+1,":")
            algorithm = input(" Enter the number of the algorithm you want to use or enter 'h' for more information on each algorithm: ")
        while algorithm not in ["1", "2", "3", "4"]:
            if algorithm == "h":
                algorithmsInfo()
                print("For level",i+1,":")
                algorithm = input(" Enter the number of the algorithm you want to use or enter 'h' for more information on each algorithm: ")
            else:
                algorithm = input("Invalid input, please try again. Enter 'h' for more information on each algorithm.: ")
        levels += [algorithm]
        decryptionKey += algorithm

    "decryptionKey is a string of the numbers of the algorithms used in the encryption"  
    "add '0's to the decryption key if the number of levels is less than 3"  
    while len(decryptionKey) < 3:
        decryptionKey += "0"

    for i in range(len(levels)):
        if levels[i] == '1':
            if i+1 == 1:
                shift = input("For the Caesar cipher of level 1, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Caesar cipher of level 1, enter the number in [0,95] by which to shift each character: ")
                "add the shift to the decryption key"
                
            elif i+1 == 2:
                shift = input("For the Caesar cipher of level 2, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Caesar cipher of level 2, enter the number in [0,95] by which to shift each character: ")
            else:
                shift = input("For the Caesar cipher of level 3, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Caesar cipher of level 3, enter the number in [0,95] by which to shift each character: ")
            if len(shift) == 1:
                    decryptionKey += "0"
            decryptionKey += shift + "0000000"
            inputText = caesar(inputText, int(shift))
        elif levels[i] == '2':
            if i+1 == 1:
                shift = input("For the Backshift cipher of level 1, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Backshift cipher of level 1, enter the number in [0,95] by which to shift each character: ")
            elif i+1 == 2:
                shift = input("For the Backshift cipher of level 2, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Backshift cipher of level 2, enter the number in [0,95] by which to shift each character: ")
            else:
                shift = input("For the Backshift cipher of level 3, enter the number in [0,95] by which to shift each character: ")
                while not validInt(shift):
                    shift = input("Invalid input. For the Backshift cipher of level 3, enter the number in [0,95] by which to shift each character: ")
            if len(shift) == 1:
                    decryptionKey += "0"
            decryptionKey += shift + "0000000"
            inputText = backshift(inputText, int(shift))
        elif levels[i] == '3':
            decryptionKey += "000000000"
            inputText = rot13(inputText)
        else:
            if i+1 == 1:
                keyword = input("For the Vigenere cipher of level 1, enter a 3-letter keyword (all lowercase) by which to map each character: ")
                while not validKeyword(keyword):
                    keyword = input("Invalid input. For the Vigenere cipher of level 1, enter a 3-letter keyword (all lowercase) by which to map each character: ")
            elif i+1 == 2:
                keyword = input("For the Vigenere cipher of level 2, enter a 3-letter keyword (all lowercase) by which to map each character: ")
                while not validKeyword(keyword):
                    keyword = input("Invalid input. For the Vigenere cipher of level 2, enter a 3-letter keyword (all lowercase) by which to map each character: ")
            else:
                keyword = input("For the Vigenere cipher of level 3, enter a 3-letter keyword (all lowercase) by which to map each character: ")
                while not validKeyword(keyword):
                    keyword = input("Invalid input. For the Vigenere cipher of level 3, enter a 3-letter keyword (all lowercase) by which to map each character: ")
            for letter in keyword:
                if len(str(ord(letter))) == 2:
                    decryptionKey += "0"
                decryptionKey += str(ord(letter))
            inputText = vigenere(inputText, keyword)
    
    
    while len(decryptionKey) < 30:
        decryptionKey += "0"
    #print(decryptionKey)
    texttofile(outputName,  decryptionKey + inputText)
    #outputName.close() 
    #print(inputText) 
    print("Your text has been encrypted successfully!")              
    break
