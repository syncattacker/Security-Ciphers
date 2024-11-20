#!/usr/bin/env python

# Import the necessary libraries
from time import sleep
from art import text2art
import os

# Function to print a nice banner.
def banner() -> None:
    '''
    Prints the banner for the Ceaser Cipher Program.
    '''
    print(text2art('\nceaser cipher', font = "usa_flag"))
    print("Developed and maintained by : @syncattacker")

# Function to clear the terminal.
def clearTerminal() -> None:
    '''
    Clear the terminal.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

# Funtion to prompt user to choose from the menu of desired actions available.
def userChoice() -> int:
    '''
    Prints a menu to the user to select operations needed to be performed.
    '''
    print("\n\n1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-Force")
    print("4. Exit\n")
    while True:
        try:
            choice = int(input("Enter the task to be performed : "))
            if (choice < 1) or (choice > 4):
                print("[-] Invalid Option.")
                continue
        except ValueError:
            print("[-] Only Integer Values Accepted.")
            continue
        else:
            return choice

# Function to encrypt the user message.
def encrypt(plainText : str, encryptionKey : int) -> str:
    '''
    Encrypt the plain text and return the encrypted text using the user key.
    '''
    cipherText = ''
    for character in plainText:
        if character.islower():
            cipherText += chr((((ord(character) - ord('a')) + encryptionKey) % 26) + ord('a'))
        elif character.isupper():
            cipherText += chr((((ord(character) - ord('A')) + encryptionKey) % 26) + ord('A'))
    return cipherText

# Function to decrypt the user message.
def decrypt(cipherText : str, decryptionKey : int) -> str:
    plainText = ''
    for character in cipherText:
        if character.islower():
            plainText += chr((((ord(character) - ord('a')) - decryptionKey) % 26) + ord('a'))
        elif character.isupper():
            plainText += chr((((ord(character) - ord('A')) - decryptionKey) % 26) + ord('A'))
    return plainText

# Function to brute force the key based on plain text and cipher text.
def bruteForce(plainText : str, cipherText : str) -> int:
    for key in range(26):
        message = encrypt(plainText, key)
        if message == cipherText:
            return key
    return None

# Function to check whether the message is only alphabets.
def validateMessage(message : str) -> bool:
    '''
    Validate user message that it does not provide any other value then alphabet
    '''
    return True if message.isalpha() else False

# Validate the user key that it only lies between 0 - 25.
def validateKey(userKey : int) -> bool:
    '''
    Validating the key entered by the user is correct or not.
    '''
    return False if ((userKey < 0) or (userKey > 25)) else True

# Handle the user message input.
def handleUserInput(inputType : str, keyType : str) -> list:
    '''
    Handles the user input for encryption of data provided by user.
    '''
    list = []
    while True:
        try:
            message = input(f"Enter Your {inputType} : ")
            if validateMessage(message):
                list.append(message)
                while True:
                    try:
                        key = int(input(f"Enter The {keyType} : "))
                        if validateKey(key):
                            list.append(key)
                            break
                    except ValueError:
                        print("[-] Invalid Key.")
                        continue
                    else:
                        print("[-] Invalid Key! Key domain 0 to 25")
                        continue
            else:
                print("[-] Invalid message, make sure it's all alphabets.")
                continue
        except Exception as error:
            print(f"Some unexpected error occured {error}")
        return list

# Handle the user message input for bruteforce.
def handleBruteForceInput(plainPrompt : str, cipherPrompt : str) -> list:
    '''
    Handles the user input for bruteforce of key with given plain text and cipher text.
    '''
    list = []
    while True:
        try:
            plainText = input(f"Enter The {plainPrompt} : ")
            if validateMessage(plainText):
                list.append(plainText)
                while True:
                    try:
                        cipherText = input(f"Enter The {cipherPrompt} : ")
                        if validateMessage(cipherText):
                            list.append(cipherText)
                            return list
                        else:
                            print("[-] Invalid message, make sure it's all alphabets.")
                            continue
                    except Exception as error:
                        print(f"Error Occured {error}")
            else:
                print("[-] Invalid message, make sure it's all alphabets.")
                continue
        except Exception as error:
            print(f"Error Occured {error}")

# Function for verbose output of brute force
def isVerbose(verbose : bool) -> None:
    pass

# Execution entry point of code.
def entryPoint() -> None:
    '''
    Main execution point of all the functions.
    '''
    clearTerminal()
    sleep(0.6)
    banner()
    while True:
        user = userChoice()
        if user == 1:
            message, key = handleUserInput('Plain Text', 'Encryption Key')
            cipherText = encrypt(message, key)
            print(f"Your Cipher Text is : {cipherText}")
        elif user == 2:
            message, key = handleUserInput('Cipher Text', 'Decryption Key')
            plainText = decrypt(message, key)
            print(f"Your Plain Text is : {plainText}")
        elif user == 3:
            plain, cipher = handleBruteForceInput('Plain Text', 'Cipher Text')
            key = bruteForce(plain, cipher)
            if key:
                print(f"Key Found : {key}")
            else:
                print("Key Not Found.")
        elif user == 4:
            exit()
entryPoint()