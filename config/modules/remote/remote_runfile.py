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

            elif line == "":
                print("\n")

            else:
                print("{}[remote] Error: Unknown command '{}'".format(Style.RESET_ALL+Fore.RED,line))


    def set(self, line):
        var = line.split(" ")

        if len(var) == 1:
            print("{}[remote] {}set >> defines variables within the environment".format(Style.BRIGHT+Fore.CYAN,Fore.BLACK))

        elif var[1] == "port":
            if len(var) == 2:
                port = var[2]
            else:
                print("{}[Cat] port >> defines the port where your server/client will start{}".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))

        elif var[1] == "inlan":
            try:
                self.server_addres = ('localhost', port)
                server_addres = self.server_addres

            except Exception as e:
                print("{}[Cat] Error: '{}' try to fix it by defining a port{}".format(Style.BRIGHT+Fore.RED,e,Style.RESET_ALL))


class SServer(CommandLine):
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(server_addres)
        server.listen(2)
        connection, addr = server.accept()

    def runserver(self)
        while True:
            op = input("\033[4;32m"+"[remote]"+"\033[0;36m"+"\033[1;36m"+"(cmd)"+"\033[0;32m > "+"\033[0;37m")
            op = op.encode()
            server.send(op)

# - Starting - #
remote_input = CommandLine()
remote_input.loop()
