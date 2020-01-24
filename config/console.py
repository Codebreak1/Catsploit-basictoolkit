# - Importing basics requirements - #
from colorama import *
from config.banners import Banners
import cmd
import os
init()

class Commands(cmd.Cmd):
    prompt = "\033[4;32m"+"[usr]"+"\033[0;32m > "+"\033[0;37m"

    def do_test(self, args):
        print("This is a simple test, working")

    def do_exit(self, args):
        print(Style.BRIGHT + Fore.CYAN + "[CS] //Leaving . . ." + Style.NORMAL)
        exit()
        os.system("cls")

    def do_banner(self, args):
        os.system("cls")
        bann = Banners()
        bann.print_banner()

    def do_cls(self, args):
        os.system("cls")
        bann = Banners()
        bann.print_banner()

    def do_import(self, args):
        actualdirectory = os.getcwd()
        module_list = os.listdir("modules")

        for args in module_list:
            pass

    def emptyline(self, args):
        print("")

    def default(self, args):
        print(Fore.RED + Style.NORMAL + "[CS] Unknown command: '{}'\n".format(args))
