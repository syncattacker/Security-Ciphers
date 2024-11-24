#!/usr/bin/env python

# Import the necessary libraries
from time import sleep
from art import text2art
import os

# Function to print a nice banner.
def banner() -> None:
    '''
    Prints the banner for the Affine Cipher Program.
    '''
    print(text2art('\naffine cipher', font = "usa_flag"))
    print("Developed and maintained by : @syncattacker")

# Function to clear the terminal.
def clearTerminal() -> None:
    '''
    Clear the terminal.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def calculateGCD( encryptionKeyOne : int, domainBlock : int) -> int:
    pass

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

