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
        print(Style.BRIGHT + Fore.CYAN + "[Cat] //Leaving . . ." + Style.NORMAL)
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
        module_list = os.listdir("config/modules")

        if args in module_list:
            if args == "r_enc":
                os.system("cd config/modules/r_enc && python r_enc_runfile.py")

            if args == "remote":
                os.system('cd config/modules/remote && python remote_runfile.py')

        else:
            print("{}[Cat] Error: Module not found\n".format(Fore.RED))

    def emptyline(self, args):
        print("")

    def default(self, args):
        print(Fore.RED + Style.NORMAL + "[Cat] Unknown command: '{}'\n".format(args))
