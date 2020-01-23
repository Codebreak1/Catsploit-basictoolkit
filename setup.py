# - Requirimientos básicos del programa - #
import os

# - Basic color requiriment - #
try:
    from colorama import *

except ImportError:
    os.system("pip install colorama -q")
init()


# - Installing r_enc requirement, cryptography - #
print("{}[Cat] {}- Cryptography requirement -".format(Fore.RED, Style.BRIGHT + Fore.BLACK))

try:
    from cryptography import *

except ImportError:
    print("{}{}[Cat] Error, missing packet > {}cryptography".format(Style.RESET_ALL, Fore.RED, Fore.GREEN))
    print("{}[Cat] Installing . . .\n".format(Style.BRIGHT + Fore.CYAN))
    os.system("pip install cryptography -q")

else:
    print("{}[Cat] Dependency already satisfied >> cryptography{}\n\n".format(Style.BRIGHT + Fore.CYAN, Style.RESET_ALL))

# - Installing r_enc requirement, login - #

print("{}[Cat] {}- Login requirement -".format(Style.RESET_ALL + Fore.RED, Fore.BLACK + Style.BRIGHT))

try:
    from login import *

except ImportError:
    print("{}{}[Cat] Error, missing packet > {}login".format(Style.RESET_ALL, Fore.RED, Fore.GREEN))
    print("{}[Cat] Installing . . .\n".format(Style.BRIGHT + Fore.CYAN))
    os.system("pip install login -q")

else:
    print("{}[Cat] Dependency already satisfied >> login\n\n".format(Style.BRIGHT + Fore.CYAN))


print("{}[Cat] All units have been installed".format(Style.RESET_ALL + Fore.GREEN))
exit()
