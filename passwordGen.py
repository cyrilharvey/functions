# Author: Cyril Harvey
# FileName: passGen.py
# Date: 11 - 06 - 2018
# Purpose: to create modified passwords

import random


def strbool(char):
    a = True
    if char == 'y':
        a = True
    elif char == 'n':
        a = False
    else:
        print("Error exiting function...")
    return a


def passgen():

    # Declares the list of available characters to the program

    s = "!@#$%^&*()"
    l = "abcdefghijklmnopqrstuvwxyz"
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "0123456789"
    comb = ""
    password = ""
    psswrd = ""

    char = int(input("How many characters should the password be? : "))
    uL = input("Should there be a mix of uppercase and lowercase characters? Defaults to lowercase. (y/n) :")
    spec = input("Should there be special characters? (y/n) :")
    num = input("Should there be numbers? (y/n) :")
    sto = input("Would you like to save the password? (y/n) : ")

    # Takes the strings given to the program by the user and throws them
    # into a function that changes them into booleans so the program
    # can use them for logical calculations

    upperLower = strbool(uL)
    special = strbool(spec)
    numbers = strbool(num)
    store = strbool(sto)

    # Determines what characters the program has at its disposal for creating
    # the password and compiles them into the string comb

    if upperLower and numbers and special:
        comb = s + l + u + n
    elif upperLower and numbers:
        comb = l + u + n
    elif numbers:
        comb = l + n
    else:
        comb = l

    # Takes the comb string and chooses reandom characters from it and formats
    # it into the string psswrd with the disired length

    # psswrd = psswrd.join(random.sample(comb, char))

    # Makes each character in the password randomized separately so that the
    # password function allows for repetition

    for i in range(char):
        psswrd += password.join(random.sample(comb, 1))

    # Decides whether the user wanted to save the password in a .txt file amd
    # collects a name, or just prints the password into the terminal

    if store:
        fileName = input("What should the password file be named?: ")
        file = open(fileName + ".txt", "w+")
        file.write(psswrd)
        print("The password file has been successfully created under the name: " + fileName)
    else:
        print("************************************")
        print("The password generated is: " + psswrd)
        print("************************************")


run = True

while run:
    print("\n")
    print("-------------------------------------")
    print(" Welcome to Cyril's garbage tune-up! ")
    print("-------------------------------------")
    print("Enter '1' for the Password Generator")
    print("Enter 'quit' to exit the program")
    fun = input("Which function would you like to run?: ")
    print("\n")

    # Decides what, if any, program the user wants to run

    if fun == "1":
        passgen()
    elif fun == "quit":
        run = False
    else:
        print("Please enter a valid input.")
