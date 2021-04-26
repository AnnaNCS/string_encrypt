from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

buffer_size = 65536 # 1024*64

def encrypt(data_to_encrypt, key):

    data = data_to_encrypt.encode('utf-8')

    # we create the cipher object and encrypt the data
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    ciphered_bytes = cipher_encrypt.encrypt(data)
    print(data_to_encrypt)

    # this is now our data 
    iv = cipher_encrypt.iv
    ciphered_data = ciphered_bytes

    print(ciphered_data)

    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
    deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)

    decrypted_data = deciphered_bytes.decode('utf-8')
    print(decrypted_data)


def main():

    key = get_random_bytes(32)

    choice = input("Type 'go' to encrypt and decrypt your text:")  

    while choice != 'Q':
        if choice == 'go':
            data_to_encrypt = input("Enter text: ")
            encrypt(data_to_encrypt, key)

        choice = input("Type 'E' to encrypt, 'D' to decrypt:")  

    print("You have quit the program");  


if __name__ == "__main__":
    main()