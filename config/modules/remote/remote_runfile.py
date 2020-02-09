import socket
import os
from colorama import *
init()

class CommandLine():
    def loop(self):
        while True:
            line = input("\033[4;32m"+"[usr]"+"\033[0;36m"+"\033[1;36m"+"(modules/remote)"+"\033[0;32m > "+"\033[0;37m")

            if line.startswith("set"):
                self.set(line)

            elif line == "exit":
                print("{}[remote] //Leaving . . .".format(Style.BRIGHT+Fore.CYAN))

            else:
                print("{}[remote] Error: Unknown command '{}'".format(Style.RESET_ALL+Fore.RED,line))


    def set(self, line):
        var = line.split(" ")

        if len(var) == 1:
            print("{}[remote] {}set >> defines variables within the environment".format(Style.BRIGHT+Fore.CYAN,Fore.BLACK))

        elif var[1] == "port":
            pass

        elif var[1] == "inlan":
            server_addres = ('localhost')
