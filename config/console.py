# - Importing basics requirements - #
from colorama import *
import cmd
init()

class Commands(cmd.Cmd):

    prompt = "\033[4;32m"+"[usr]"+"\033[0;32m > "+"\033[0;37m"
