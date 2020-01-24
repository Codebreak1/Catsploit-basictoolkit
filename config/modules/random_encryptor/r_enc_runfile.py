from Random_Encrypt import *
from colorama import *
import cmd
init()
print("{}[Cat] Imported module{}".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))


class Random_Enc(cmd.Cmd):
    prompt = "\033[4;32m"+"[usr]"+"\033[1;36m"+"(modules/r_enc)"+"\033[0;32m > "+"\033[0;37m"

    def do_help(self, args):
        print("""{}[r_enc] {}displaying information about r_enc >>
        -> The program encrypts text based on a random algorithm.
           So when you start make sure you save your key,
           then load it and be able to decrypt it without problems

         -> {}Save key: {}r_enc save_key (path)
         -> {}Load key: {}r_enc load_key (path)
         -> {}Encrypt text: {}r_enc encrypt (text)
         -> {}Decrypt text: {}r_enc decrypt (text)
         -> {}Encrypt file: {}r_enc encrypt_file (input path) (output path)
         -> {}Decrypt file: {}r_enc decrypt_file (input path) (output path){}"""
         .format(Style.BRIGHT+Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore,CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Style.RESET_ALL))

    def r_enc(self, args):
        if args == "encrypt":
            print(Fore.LIGHTYELLOW_EX+" [r_enc] Encrypted text : {}".format(self.random_encryptor.encrypt_text(options[2]))+Fore.LIGHTWHITE_EX)

        elif args == "decrypt":
            print(Fore.LIGHTYELLOW_EX+" [r_enc] Decrypted text : {}".format(self.random_encryptor.decrypt_text(options[2])), Fore.LIGHTWHITE_EX)

        elif args == "save_key":
            self.random_encryptor.save_key(options[2])
            print(Fore.LIGHTYELLOW_EX+"Done!."+Fore.LIGHTWHITE_EX)

        elif args == "load_key":
            self.random_encryptor.load_key(options[2])
            print(Fore.LIGHTYELLOW_EX+"Done!."+Fore.LIGHTWHITE_EX)

        elif args == "encrypt_file":
            try:
                self.random_encryptor.encrypt_file(options[2], options[3])
                print(Fore.LIGHTYELLOW_EX+" [r_enc] Done!."+Fore.LIGHTWHITE_EX)
            except:
                log.error("Error!", exc_info=True)
                print(Fore.LIGHTRED_EX+" [r_enc] Apparently something went wrong. For more information, see log.txt")

        elif args == "decrypt_file":
            try:
                self.random_encryptor.decrypt_file(options[2], options[3])
                print(Fore.LIGHTYELLOW_EX+" [*] Hecho!." + Fore.LIGHTWHITE_EX)
            except:
                log.error("Error!", exc_info=True)
                print(Fore.LIGHTRED_EX + "Apparently something went wrong. For more information, see log.txt")

    def emptyline(self, args):
        print("")

    def default(self, args):
        print(Fore.RED + Style.NORMAL + "[r_enc] Unknown command: '{}'\n".format(args))
