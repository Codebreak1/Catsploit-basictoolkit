# - Importing basics requirements - #
from colorama import *
import cmd
import banners
init()

class Commands(cmd.Cmd):
    prompt = "\033[4;32m"+"[usr]"+"\033[0;32m > "+"\033[0;37m"

    def do_test(self, args):
        print("This is a simple test, working")

    def do_exit(self, args):
        print("Exit")
        exit()

    def do_banner(self, args):
            print_banner()

console = Commands()
console.cmdloop()
