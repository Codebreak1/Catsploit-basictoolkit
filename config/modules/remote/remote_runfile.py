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

            elif line == "runserver":
                try:
                    obj_server = SServer()
                    obj_server.runserver()

                except Exception as e:
                    print("{}[Cat] Error: '{}'{}".format(Style.BRIGHT+Fore.RED,e,Style.RESET_ALL))

            elif line == "exit":
                print("{}[remote] //Leaving . . .\n".format(Style.BRIGHT+Fore.CYAN))
                exit()

            elif line == "":
                print("")

            else:
                print("{}[remote] Error: Unknown command '{}'\n".format(Style.RESET_ALL+Fore.RED,line))


    def set(self, line):
        var = line.split(" ")
        print(var)

        if len(var) == 1:
            print("{}[remote] {}set >> defines variables within the environment\n".format(Style.BRIGHT+Fore.CYAN,Fore.BLACK))

        elif var[1] == "port":
            if len(var) == 3:
                port = var[2]
                port = int(port)
                print(port)

            else:
                print("{}[Cat] port >> defines the port where your server/client will start{}\n".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))

        elif var[1] == "inlan":
            try:
                print(port)
                self.server_addres = ('localhost', port)
                server_addres = self.server_addres

            except Exception as e:
                print("{}[Cat] Error: '{}' try to fix it by defining a port{}\n".format(Fore.RED,e,Style.RESET_ALL))

        else:
            print("{}[Cat] Unknown argument '{}'{}\n".format(Fore.RED,var[1],Style.RESET_ALL))

class SServer(CommandLine):
    def runserver(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(server_addres)
        server.listen(2)
        connection, addr = server.accept()

        while True:
            op = input("\033[4;32m"+"[remote]"+"\033[0;36m"+"\033[1;36m"+"(cmd)"+"\033[0;32m > "+"\033[0;37m")
            op = op.encode()
            server.send(op)

            op = op.decode()

            if op == "exit":
                print("{}- connection terminated -{}".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))
                connection.close()
                server.close()
                break

# - Starting - #
remote_input = CommandLine()
remote_input.loop()
