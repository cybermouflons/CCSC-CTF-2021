#! /usr/bin/python3
#-*- coding:utf-8 -*-
import base64
import sys
def main():

    print("========================================================================")
    print(" _____       _   _                   _____           _        _ ")
    print("|  __ \     | | | |                 |  __ \         | |      | |")
    print("| |__) |   _| |_| |__   ___  _ __   | |__) |__  _ __| |_ __ _| |")
    print("|  ___/ | | | __| '_ \ / _ \| '_ \  |  ___/ _ \| '__| __/ _` | |")
    print("| |   | |_| | |_| | | | (_) | | | | | |  | (_) | |  | || (_| | |")
    print("|_|    \__, |\__|_| |_|\___/|_| |_| |_|   \___/|_|   \__\__,_|_|")
    print("        __/ |                                                   ")
    print("       |___/                                                    ")
    print("========================================================================")
    print("Here our developers can write their python scripts to help \nchess players analyze and improve their game.")
    print("========================================================================")
    print("                                                      .::.           ")
    print("                                           _()_       _::_           ")
    print("                                 _O      _/____\_   _/____\_         ")
    print("          _  _  _     ^^__      / //\    \      /   \      /         ")
    print("         | || || |   /  - \_   {     }    \____/     \____/          ")
    print("         |_______| <|    __<    \___/     (____)     (____)          ")
    print("   _     \__ ___ / <|    \      (___)      |  |       |  |           ")
    print("  (_)     |___|_|  <|     \      |_|       |__|       |__|           ")
    print(" (___)    |_|___|  <|______\    /   \     /    \     /    \          ")
    print(" _|_|_    |___|_|   _|____|_   (_____)   (______)   (______)         ")
    print("(_____)  (_______) (________) (_______) (________) (________)        ")
    print("/_____\  /_______\ /________\ /_______\ /________\ /________\        ")
    print("========================================================================")
    print("Created by your lord and savior   [ R3D ]\n\n")
    text = input('>>> ')
    for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write','+','cat']:
        if keyword in text.lower():
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print("Oh no you didn't!!! \\o \nTry again friend...\n\n")
            return;
        elif 'exit' in text.lower():
            exit()
    else:
        exec(text)
if __name__ == "__main__":
    while 1:
        main()
       
