#Файл зашифрован с помощью simple-crypt
import simplecrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    with open("passwords.txt", "rb") as p:
        pwds=p.read().splitlines()
        for pwd in pwds:
            try:
                print(simplecrypt.decrypt(pwd, encrypted))
            except Exception:
                pass
