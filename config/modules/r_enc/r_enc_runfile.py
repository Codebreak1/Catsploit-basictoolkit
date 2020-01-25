from Random_Encrypt import *
from colorama import *
init()
print("{}[Cat] Imported module{}\n".format(Style.BRIGHT+Fore.CYAN,Style.RESET_ALL))


class Random_Enc():
    def __init__(self):
        self.random_encryptor=Random_Encrypt()

    def menu(self):
        while True:
            op = input("\033[4;32m"+"[usr]"+"\033[0;36m"+"\033[1;36m"+"(modules/r_enc)"+"\033[0;32m > "+"\033[0;37m")
            self.functions(op)

    def functions(self, op):
        if op.startswith("r_enc"):
            self.r_enc(op)

        elif op == "exit":
            print(Style.BRIGHT + Fore.CYAN + "[r_enc] //Leaving . . .\n" + Style.NORMAL)
            exit()

        else:
            print(Fore.RED + Style.NORMAL + "[r_enc] Unknown command: '{}'\n".format(op))

    def r_enc(self, op):
        options=op.split(" ")
        if len(options)==1:
            print("""{}\n [r_enc] {}displaying information about r_enc >>
            -> The program encrypts text based on a random algorithm.
            So when you start make sure you save your key,
            then load it and be able to decrypt it without problems

            -> {}Save key: {}r_enc save_key (path)
            -> {}Load key: {}r_enc load_key (path)
            -> {}Encrypt text: {}r_enc encrypt (text)
            -> {}Decrypt text: {}r_enc decrypt (text)
            -> {}Encrypt file: {}r_enc encrypt_file (input path) (output path)
            -> {}Decrypt file: {}r_enc decrypt_file (input path) (output path){}\n"""
            .format(Style.BRIGHT+Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Fore.CYAN,Fore.BLACK,Style.RESET_ALL))

        elif options[1]=="encrypt":
            print(Fore.LIGHTYELLOW_EX+" [r_enc] Encrypted text : {}\n".format(self.random_encryptor.encrypt_text(options[2]))+Fore.LIGHTWHITE_EX)

        elif options[1]=="decrypt":
            print(Fore.LIGHTYELLOW_EX+" [r_enc] Decrypted text : {}\n".format(self.random_encryptor.decrypt_text(options[2])), Fore.LIGHTWHITE_EX)


        elif options[1]=="encrypt_file":
            try:
                self.random_encryptor.encrypt_file(options[2], options[3])
                print(Fore.LIGHTYELLOW_EX+"[r_enc] Done!\n"+Fore.LIGHTWHITE_EX)
            except:
                log.error("Error!", exc_info=True)
                print(Fore.LIGHTRED_EX+"[r_enc] Apparently something went wrong. For more information, see log.txt\n")

        elif options[1] == "decrypt_file":
            try:
                self.random_encryptor.decrypt_file(options[2], options[3])
                print(Fore.LIGHTYELLOW_EX+"[r_enc] Done!\n" + Fore.LIGHTWHITE_EX)
            except:
                log.error("Error!", exc_info=True)
                print(Fore.LIGHTRED_EX + "[r_enc] Apparently something went wrong. For more information, see log.txt\n")

        elif options[1]=="save_key":
            self.random_encryptor.save_key(options[2])
            print(Fore.LIGHTYELLOW_EX+"[r_enc] Done!\n"+Fore.LIGHTWHITE_EX)

        elif options[1]=="load_key":
            self.random_encryptor.load_key(options[2])
            print(Fore.LIGHTYELLOW_EX+"[r_enc] Done!\n"+Fore.LIGHTWHITE_EX)

run_renc = Random_Enc()
run_renc.menu()
