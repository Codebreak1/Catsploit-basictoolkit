import socket
import os
from colorama import *
init()
print("{}[Cat] Imported module{}\n".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))


class CommandLine():
    def __init__(self):
        self.server_addres = ()
        server_addres = self.server_addres

    def loop(self):
        while True:
            line = input("\033[4;32m"+"[usr]"+"\033[0;36m"+"\033[1;36m"+"(modules/remote)"+"\033[0;32m > "+"\033[0;37m")

            if line.startswith("set"):
                self.set(line)

            elif line == "run":
                try:
                    print("\n{}Waiting answer . . .{}".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))
                    server = socket.socket()
                    server.bind(('localhost', 8000)) #FIX THIS!!!
                    server.listen(2)
                    connection, addr = server.accept()
                    print("{} >> established connection <<{}\n".format(Fore.MAGENTA + Style.BRIGHT, Style.RESET_ALL))

                    while True:
                        op = input("\033[4;31m"+"[remote]"+"\033[0;36m"+"\033[1;33m"+"(cmd)"+"\033[0;32m > "+"\033[0;37m")
                        op = op.encode()
                        connection.send(op)

                        op = op.decode()
                        client_output = connection.recv(3072)
                        client_output = client_output.decode()
                        if client_output == "" or client_output == None:
                            print("empty")
                            pass
                        else:
                            print(client_output)

                        if op == "exit":
                            print("{}- connection terminated -{}\n".format(Style.BRIGHT+Fore.RED,Style.RESET_ALL))
                            connection.close()
                            server.close()
                            break

                except Exception as e:
                    print("{}[Cat] Error: '{}'{}\n".format(Fore.RED,e,Style.RESET_ALL))

            elif line == "exit":
                print("{}[remote] //Leaving . . .\n".format(Style.BRIGHT+Fore.CYAN))
                exit()

            elif line == "":
                print("")

            else:
                print("{}[remote] Error: Unknown command '{}'\n".format(Style.RESET_ALL+Fore.RED,line))


    def set(self, line):
        var = line.split(" ")
        #print(var)

        if len(var) == 1:
            print("{}[remote] {}set >> defines variables within the environment{}\n".format(Style.BRIGHT+Fore.CYAN,Fore.BLACK,Style.RESET_ALL))

        elif var[1] == "port":
            if len(var) == 3:
                lport = 8000
                #print(lport)
                if var[2] == "inlan":
                    try:
                        #print(lport)
                        self.server_addres = ('localhost', lport)
                        print("{}[remote] Done!{}\n".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))

                    except Exception as e:
                        print("{}[remote] Error: '{}' try to fix it by defining a port{}\n".format(Fore.RED,e,Style.RESET_ALL))

                else:
                    print("{}[remote] Error: required argument 'in/outlan'{}\n".format(Fore.RED,Style.RESET_ALL))

            else:
                print("{}[remote] Error: required arguments{}\n".format(Fore.RED,Style.RESET_ALL))

        else:
            print("{}[remote] Unknown argument '{}'{}\n".format(Fore.RED,var[1],Style.RESET_ALL))


# - Starting - #
remote_input = CommandLine()
remote_input.loop()
