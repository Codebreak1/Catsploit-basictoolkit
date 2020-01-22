from colorama import *
from random import randint

class Banners():
    def print_banner(self):
        bannern = randint(0,3)
        print(bannern)

        if bannern == 1:
            print(Fore.LIGHTBLACK_EX+"[CS] [0.0.1] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []\n")
            print(Fore.GREEN+"> hack\t\t\t\t\t\t\t  "+Fore.LIGHTBLACK_EX+"[]")
            print(Fore.LIGHTBLACK_EX+"[*] Downloading website . . .\t[Sesion1]")
            print("     #Installing backdoor\t[Sesion1-TheFatRat]\t  []")
            print("     #Connecting to TheFatRat\t[Sesion1-TheFatRat]")
            print(Fore.LIGHTGREEN_EX+"//Succesfuly \t[Sesion1]\t\t\t\t  "+Fore.LIGHTBLACK_EX+"[]\n"+Fore.GREEN)
            print(Fore.LIGHTBLACK_EX+" [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []\n")
            count1 = 1

        elif bannern == 2:
            print(Fore.RED+Style.NORMAL)
            print(r"     ________________________")
            print(r"    |                        |")
            print(r"    |   RipPrivacy           |")
            print(r"    |                        |")
            print(r" ___|	        [Catsploit]  |")
            print(r" \ _|                        |")
            print(r"  \\|                        |")
            print(r"   \|________________________|"+Fore.RESET)
            print("")
            count1 = 2

        elif bannern == 3:
            print(Fore.GREEN + Style.NORMAL)
            print(r"_________v1.0     __   _________      .__         .__  __   ")
            print(r"\_   ___ \_____ _/  |_/   _____/_____ |  |   ____ |__|/  |_ ")
            print(r"/    \  \/\__  \\   __\_____  \\____ \|  |  /  _ \|  \   __.")
            print(r"\     \____/ __ \|  | /        \  |_> >  |_(  <_> )  ||  |  ")
            print(r" \______  (____  /__|/_______  /   __/|____/\____/|__||__|  ")
            print(r"        \/     \/            \/|__|                         ")
            print("")
            count1 = 3

        print(Fore.WHITE+"""\
    <<--[[ """+Fore.MAGENTA+"""CatSploit v1.0"""+Fore.WHITE+""" ]}

            __-[0 exploits - 0 addons  - 0 frameworks]-__
            __-[2 develops - 2 modules - 3 banners   ]-__ by Catsploit & Kalinka\n""")

test = Banners()
test.print_banner()
