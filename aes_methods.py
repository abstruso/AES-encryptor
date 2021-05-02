import hash_methods
import sty


def aes_demonstration():
    """Used encyption and decyption algorithms based on:
    https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto"""

    print("This method operates on file example_file.txt")
    plain_filename = "example_file.txt"
    enc_filename = plain_filename + ".aes"
    file = open(plain_filename, "w+")  # creates a file with permission to write
    file.write("This is sample content")
    print("part I - file encryption and decryption")

    try:
        file = open(plain_filename)
    except IOError:
        print(sty.fg.yellow + "[!] " + sty.fg.yellow + "File not accessible, creating new one")
        file = open("example_file.txt", "w+")
        file.write("This is sample content")
        file.close()
    finally:
        aes_encryption(input_key(), file, enc_filename)
        print(plain_filename, "has now encrypted version", enc_filename)
        input("Press Enter to proceed with decryption and delete orginal file")
        aes_decryption(input_key(), enc_filename)


def input_key():
    """Prompts user about key and adjusts it length"""
    import hashlib
    import getpass
    password = getpass.getpass("Please enter password: ").encode('utf-8')
    key = hashlib.sha256(password).digest()
    return key


def generate_random_iv():
    """Generates random 16 bytes initial vector"""
    import Crypto.Random.random
    initialization_vector = "".join(chr(Crypto.Random.random.randint(32, 127)) for i in range(16))
    return initialization_vector.encode('utf-8')


def file_encryption(file_name):
    file = open(file_name)
    file.close()
    aes_encryption(input_key(), file, file.name + ".aes")


def aes_encryption(key, file, enc_filename):
    """Short demonstration of AES-128 encrypting text files"""
    import os
    import struct
    import Crypto.Cipher.AES
    chunksize = 65536
    initialization_vector = generate_random_iv()
    print(sty.fg.green + "[+] " + sty.fg.rs + "initialization vector:", initialization_vector)
    encryptor = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, initialization_vector)
    filesize = os.path.getsize(file.name)

    with open(file.name, 'rb') as infile:
        with open(enc_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            # struct.pack('<ii', long, long >> 32) is equivalent to '<q'
            outfile.write(initialization_vector)
            outfile.write(hash_methods.file_hash(file.name))

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk_padding = (' ' * (16 - len(chunk) % 16))
                    chunk_padding = str(chunk_padding).encode('utf-8')
                    chunk += chunk_padding

                outfile.write(encryptor.encrypt(chunk))
    print(sty.fg.green + "[+] " + sty.fg.rs + "File successfully encrypted")


def file_decryption(file_name):
    check_extension(file_name)
    aes_decryption(input_key(), file_name)


def aes_decryption(key, enc_filename):
    """Short demonstration of AES-128 decrypting text files"""
    import os
    import struct
    from Crypto.Cipher import AES

    chunksize = 24576

    plain_filename = os.path.splitext(enc_filename)[0]

    with open(enc_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        initialization_vector = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, initialization_vector)
        readed_hash = infile.read(64)

        with open(plain_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                if len(chunk) % 16 != 0:
                    print(sty.fg.yellow + "[!] " + sty.fg.rs + "Ciphertext format error")
                    break
                outfile.write(decryptor.decrypt(chunk))
            try:
                outfile.truncate(origsize)
            except:
                print(sty.fg.red + "[-] " + sty.fg.rs + "invalid file")

        outfile_hash = hash_methods.file_hash(outfile.name)
        if outfile_hash == readed_hash:
            print(sty.fg.green + "[+] " + sty.fg.rs + "File successfully decrypted, hashes match\nhash:", outfile_hash)
        else:
            print(sty.fg.yellow + "[!] " + sty.fg.rs + "Hashes don't match")
            print(" - password is invalid, or")
            print(" - cipher text is damaged")
            print("readed hash                ", outfile_hash)
            print("passed hash of orginal file", readed_hash)


def check_extension(file_name):
    if not str(file_name).endswith(".aes"):
        print(sty.fg.yellow + "[!] " + sty.fg.rs +
              "this file is propably incorrect")
