#!/usr/bin/env python

# Import the necessary libraries
import time
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
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-Force")
    print("4. Exit")

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
    pass

