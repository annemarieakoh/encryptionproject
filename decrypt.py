from pathlib import Path
import os
"program to take a file and decrypt it or to take a user input string and decrypt it"
"saves decrypted text to a new file"

def decryptCaesar(ciphertext, shift):
    decryption = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) == 10:
            decryption += "\n"
        elif ord(ciphertext[i]) - shift < 32:
            decryption += chr(126 - (shift - (ord(ciphertext[i]) - 31)))
        else:
            decryption += chr(ord(ciphertext[i]) - shift)
    return decryption

def decryptBackshift(ciphertext, shift):
    decryption = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) == 10:
            decryption += "\n"
        elif ord(ciphertext[i]) + shift > 126:
            decryption += chr(31 + (shift - (126 - ord(ciphertext[i]))))
        else:
            decryption += chr(ord(ciphertext[i]) + shift)
    return decryption

def decryptRot13(ciphertext):
    decryption = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) == 10:
            decryption += "\n"
        elif ord(ciphertext[i]) - 13 < 32:
            decryption += chr(126 - (13 - (ord(ciphertext[i]) - 31)))
        else:
            decryption += chr(ord(ciphertext[i]) - 13)
    return decryption

def decryptVigenere(ciphertext, keyword):
    decryption = ""
    "modifying the keyword to match the length of the ciphertext"
    index = 0
    while not (len(keyword) == len(ciphertext)):
        if len(keyword) > len(ciphertext):
            while len(keyword) > len(ciphertext):
                keyword = keyword[:-1]
                if len(keyword) == len(ciphertext):
                    break
        else:
            keyword += keyword[index]
            index += 1
    for i in range(len(keyword)):
        if ord(ciphertext[i]) == 10:
            decryption += "\n"
            continue
        row = ord(keyword[i])
        rounds = 0
        #print("row:", row)
        offset = 0
        while chr(row + offset) != ciphertext[i]:
            if (row + offset) > 126:
                #row = ((row + offset) % 126) + 31
                row = 32
                offset = -1
            offset += 1
            rounds += 1
            #print("row:",row,"rounds:",rounds,"curr:", chr(row + offset), "target:", ciphertext[i])
        #print("rounds:", rounds)
        decryption += chr(((rounds + 31) % 95) + 32)
        #decryption += chr((rounds + 31) + 32)
        #decryption += chr(rounds + 32)
    #print(decryption)
    return decryption



def texttofile(filename, txt):
    "creates or opens the file called 'filename' and writes the txt to it"
    file = open(filename, "w")
    file.write(txt)
    return

def validDecryption(string):
    "checks for valid decryption key at beginning of string"
    for i in range(31):
        if int(string[i]) < 0 or int(string[i]) > 9:
            return False
    return True

while(True):
    inputType = input("Enter 1 to decrypt an existing text file or 2 to type something to decrypt: ")
    while inputType not in ["1","2"]:
        inputType = input("Invalid input, please try again. Enter 1 to decrypt an existing text file or 2 to type something to decrypt: ")
    if(inputType == "1"):
        inputFileName = input("Enter the name of the file you want to decrypt: ")
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
        createFile = input("Enter the name of the file you want to write your encrypted text to: ")
        while len(createFile) == 0:
            createFile = input("Invalid input, please try again. Enter the name of the file you want to write your encrypted text to: ")
        inputText = input("Enter the text you want to decrypt: ")
        while not validDecryption(inputText):
            inputText = input("Invalid input, please try again. Enter the text you want to decrypt: ")
        texttofile(createFile, inputText)

    outputName = input("Enter the name of the file you want to save the decrypted text to: ")
    while len(outputName) == 0:
        outputName = input("Invalid input, please try again. Enter the name of the file you want to save the decrypted text to: ")
    outputFile = open(outputName, "w")

    "holds 3-bits about which algorithms were used to encrypt the text"
    algorithms = inputText[:3]

    "holds specific information in 9-bits about corresponding encryption algorithm"
    decryptionKey = inputText[3:30]

    "holds the encrypted text"
    inputText = inputText[30:]

    #print("before:",inputText)

    for i in range(len(algorithms)):
        if algorithms[i] == "1":
            start = i*9
            end = start + 9
            shift = decryptionKey[start:end]
            shift = shift[:2]
            inputText = decryptCaesar(inputText, int(shift))
            #print("caesar shift:", shift)
        elif algorithms[i] == "2":
            start = i*9
            end = start + 9
            shift = decryptionKey[start:end]
            shift = shift[:2]
            inputText = decryptBackshift(inputText, int(shift))
            #print("backshift shift:",shift)
        elif algorithms[i] == "3":
            inputText = decryptRot13(inputText)
        elif algorithms[i] == "4":
            start = i*9
            end = start + 9
            asciiCode = decryptionKey[start:end]
            keyword = ""
            index = 0
            while index < 7:
                keyword += chr(int(asciiCode[index:index+3]))
                index += 3
            inputText = decryptVigenere(inputText, keyword)
        

    
    #print(algorithms)   
    #print(decryptionKey)
    #print(inputText)
    #print(decryptionKey)
    #print("after:",inputText)
    texttofile(outputName, inputText)
    outputFile.close()
    print("Your text has been decrypted successfully!") 
    break

    
