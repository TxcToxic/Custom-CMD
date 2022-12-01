import os
from time import sleep
import webbrowser
import sys

import colorama
import requests
import socket
from colorama import Fore, Back, Style

scp = False  # Automated method
pVersion = "1.3.1"  # Update
cVersion = requests.get("http://cft-devs.xyz/custom-cmd/index.json").json()["version"]


def updateCheck():
    if pVersion == cVersion:
        return True
    else:
        return False


def logoPrint():
    os.system("title CMD by CFT-Development")
    os.system("clear || cls")
    print(Fore.RED + r""" __     ____   __  __   ____     __
 \ \   / ___| |  \/  | |  _ \   / /
  \ \ | |     | |\/| | | | | | / / 
  / / | |___  | |  | | | |_| | \ \ 
 /_/   \____| |_|  |_| |____/   \_\
         by CFT-Development        
          ! Windows ONLY !         
""" + Style.RESET_ALL)


def print2(value: str, breaklineend: bool = True, breaklinestart: bool = False):
    if breaklinestart:
        sys.stdout.write("\n")
        sys.stdout.flush()
    sys.stdout.write(" ")
    for letter in value.replace('\n', '\n '):
        sys.stdout.write(f"{letter}")
        sys.stdout.flush()
        sleep(.01)
    if breaklineend:
        sys.stdout.write("\n")
        sys.stdout.flush()


def close():
    logoPrint()
    print2(Fore.YELLOW + "Closing program in 3 seconds", breaklineend=False)
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(1)
    print(Style.RESET_ALL)
    quit()


if __name__ == "__main__":
    colorama.init()
    if not os.name == "nt":
        print("Program only works on windows!")
        while True:
            sleep(100)
    os.system("color 4")
    logoPrint()
    if not updateCheck():
        print2("A newer version is available!")
        print(f"\n"
              f" Current Version : " + Fore.GREEN + f"{cVersion}\n" + Style.RESET_ALL +
              f" Your Version    : " + Fore.RED + f"{pVersion}" + Style.RESET_ALL)
        print2("download? (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")", breaklinestart=True)
        ask = input("\n (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")> ")
        if ask in ("yes", "y"):
            url = 'http://cft-devs.xyz/custom-cmd/dl/Custom%20CMD.exe'
            webbrowser.open(url, new=True)
            sleep(2)
            close()
        else:
            print2("[" + Fore.RED + "ERROR" + Fore.RESET + "] Cancelled update, closing...")
            sleep(2)
            close()
    while True:
        try:
            cmd = input(f" {'$' if not scp else f'{os.getcwd()}'}" + Fore.LIGHTBLACK_EX + "> " + Style.RESET_ALL)
        except KeyboardInterrupt:
            print2("Are you sure? (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")")
            ask = input(f"\n (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")> ")
            if ask.casefold() in ("y", "yes"):
                close()
            cmd = ""
        cmd2 = cmd.casefold()
        if cmd2 in ("help", "-h"):
            print(Fore.LIGHTBLACK_EX + " Commands:\n" + Fore.RESET)
            print2("          -h : help    | -au : about    | -c : clear | -e : exit | -sp : showpath | -ip : ipinfo\n"
                   "          ls : listdir | -sd : shutdown |")
        elif cmd2 in ("about", "-au"):
            print2("This is a custom CMD was made by -TOXIC-#1835 (" + Fore.RED + "CFT-Development" + Fore.RESET + ")\n\n"
                   "Registered commands under '" + Fore.LIGHTBLACK_EX + "help" + Fore.RESET + "' any other commands will be executed like in the main CMD")
            webbrowser.open(url="http://cft-devs.xyz", new=True)
        elif cmd2 in ("clear", "cls", "-c"):
            logoPrint()
        elif cmd2.startswith("title"):
            args = cmd.split(" ")
            txt = " ".join(args[1:])
            os.system("title CMD by CFT-Development: {}".format(txt))
        elif cmd2 in ("cmd", "powershell"):
            print2("[" + Fore.RED + "ERROR" + Fore.RESET + "] Can't open other commanders trough this CMD")
        elif cmd2 in ("quit", "exit", "-e", "close"):
            print2("Are you sure? (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")")
            try:
                ask = input(f"\n (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")> ")
            except KeyboardInterrupt:
                quit()
            if ask.casefold() in ("y", "yes"):
                close()
        elif cmd2.startswith("cd"):
            args = cmd.split(" ")
            txt = " ".join(args[1:])
            os.chdir(txt)
            print2(f"Current directory > {os.getcwd()}")
        elif cmd2.startswith(("-sp", "showpath")):
            args = cmd.split(" ")
            txt = " ".join(args[1:])
            if txt in ("enable", "-e"):
                scp = True
            elif txt in ("disable", "-d"):
                scp = False
            else:
                print2("[" + Fore.RED + "ERROR" + Fore.RESET + "] Unkown argument!\n\n"
                       "Args: -d | disable (Default), -e | enable")
        elif cmd2 in ("ls", "listdir"):
            fileList = "\n".join(os.listdir())
            for fod in fileList.split("\n"):
                if os.path.isfile(fod):
                    if fod.startswith("."):
                        print(f" {fod} : File : hidden")
                    else:
                        print(f" {fod} : File")
                elif os.path.isdir(fod):
                    if fod.startswith("."):
                        print(Back.RESET + " [" + Back.LIGHTBLACK_EX + f"{fod}" + Back.RESET + "] : Dir : hidden")
                    else:
                        print(Back.RESET + " [" + Back.WHITE + Fore.BLACK + f"{fod}" + Style.RESET_ALL + "] : Dir")
            print2("For more Information type 'dir /?'", breaklinestart=True)
        elif cmd2.startswith(("-ip", "ipinfo")):
            pubip = requests.get("http://ipinfo.io/json", allow_redirects=True).json()["ip"]
            intip = socket.gethostbyname(socket.gethostname())
            print2("Your " + Fore.BLUE + "public" + Fore.RESET + f" IP-Address   > {pubip}\n"
                   "Your " + Fore.CYAN + "internal" + Fore.RESET + f" IP-Address > {intip}")
        elif cmd2 in ("-sd", "shutdown"):
            logoPrint()
            print2(Fore.YELLOW + "Shutdown in 3 seconds", breaklineend=False)
            timer = 3
            while timer > 0:
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(1)
                timer -= 1
            print(Style.RESET_ALL)
            os.system("shutdown /f /p")
        else:
            os.system(cmd)
