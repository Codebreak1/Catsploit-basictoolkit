from config.console import *
from config.banners import *
try:
    from colorama import *
except ImportError:
    print("\033[;31"+"[CS] Main module 'colorama', not found")
    print("-> Fix it by running setup.py 'python setup.py' <-")


# - Calling main functions - #
bann = Banners()
bann.print_banner()
console = Commands()
console.cmdloop()
