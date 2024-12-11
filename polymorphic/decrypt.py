#incase if you encrypt you files. this code can decrypt it back
#https://github.com/amiroooamiran/Malware-with-python/
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():

    if file == "metamorphic_malware.py" or file == "secret.key" \
    or file == "polymorphic_malware.py" or file == "" or \
    file == "malware.bin" or file == "polymorphic_loader.py":
        continue

    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)