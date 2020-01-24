from cryptography.fernet import Fernet
from pickle import load,dump

class Random_Encrypt():
    def __init__(self):
        self.key=Fernet.generate_key()
        self.code=Fernet(self.key)

    def encrypt_text(self, text):
        texto=text.encode()
        enc_text=self.code.encrypt(texto)
        return enc_text.decode()

    def decrypt_text(self, text):
        texto=text.encode()
        dec_text=self.code.decrypt(texto)
        return dec_text.decode()

    def encrypt_file(self, file, output):
        with open(file, "rb") as f:
            data=f.read()
        data_encrypted=self.code.encrypt(data)

        with open(output, "wb") as f:
            dump(data_encrypted, f)

    def decrypt_file(self, file, output):
        with open(file, "rb") as f:
            data=load(f)
        data_decrypted=self.code.decrypt(data)

        with open(output, "wb") as f:
            f.write(data_decrypted)

    def save_key(self, path):
        with open(path+".data", "wb") as f:
            dump(self.key, f)

    def load_key(self, path):
        with open(path, "rb") as f:
            self.code=Fernet(load(f))

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.code = Fernet(self.key)