from colorama import *
init()

class InputC():
    def entry(self):
        while True:
            command = input(Fore.GREEN + "[usr] > ")
            self.execute(command)

    def execute(self, command):
        if command == "help":
            
