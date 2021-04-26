from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

buffer_size = 65536 # 1024*64

def encrypt(file_to_encrypt, key):

    # open the file in binary mode
    input_file = open(file_to_encrypt, 'rb') 
    # file opened for binary writing 
    output_file = open('encrypted_' + file_to_encrypt, 'wb')

    # Create a new AES cipher
    cipher_encrypt = AES.new(key, AES.MODE_CFB) 
    # Cipher FeedBack Mode -> 
        # Each underlying block cipheris transforms into a stream cipher. 
        # Plaintext and ciphertext are processed in segments of x bits. 

    output_file.write(cipher_encrypt.iv)

    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        ciphered_bytes = cipher_encrypt.encrypt(buffer)
        output_file.write(ciphered_bytes)
        buffer = input_file.read(buffer_size)

    input_file.close()
    output_file.close()

def decrypt(file_to_encrypt, key):

    input_file = open('encrypted_' + file_to_encrypt, 'rb')
    output_file = open('decrypted_' + file_to_encrypt, 'wb')

    iv = input_file.read(16)

    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv=iv)

    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        decrypted_bytes = cipher_encrypt.decrypt(buffer)
        output_file.write(decrypted_bytes)
        buffer = input_file.read(buffer_size)

    input_file.close()
    output_file.close()


def main():

    key = get_random_bytes(32)

    choice = input("Type 'E' to encrypt, 'D' to decrypt:")  

    while choice != 'Q':
        if choice == 'E':
            file_to_encrypt = input("Enter the file name: ")
            encrypt(file_to_encrypt, key)

        if choice == 'D':
            file_to_decrypt = input("Enter the file name: ")
            decrypt(file_to_decrypt, key)

        choice = input("Type 'E' to encrypt, 'D' to decrypt:")  

    print("You have quit the program");  


if __name__ == "__main__":
    main()