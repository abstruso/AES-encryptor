import hash_methods
import sty


def aes_demonstration():
    """Used encyption and decyption algorithms based on:
    https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto"""

    print("This method operates on file example_file.txt")
    plain_filename = "example_file.txt"
    enc_filename = plain_filename + ".aes"
    f = open(plain_filename, "w+")  # creates a file with permission to write
    f.write("This is sample content")
    print("part I - file encryption and decryption")

    try:
        f = open(plain_filename)
    except IOError:
        print(sty.fg.yellow + "[!] " + sty.fg.yellow + "File not accessible, creating new one")
        f = open("example_file.txt", "w+")
        f.write("This is sample content")
        f.close()
    finally:
        aes_encryption(input_key(), f, enc_filename)
        print(plain_filename, "has now encrypted version", enc_filename)
        input("Press Enter to proceed with decryption and delete orginal file")
        aes_decryption(input_key(), enc_filename)


def input_key():
    """Prompts user about key and adjusts it length"""
    import hashlib
    password = input("Please enter password: ").encode('utf-8')
    key = hashlib.sha256(password).digest()
    return key


def generate_random_iv():
    """Generates random 16 bytes initial vector"""
    import Crypto.Random.random
    iv = "".join(chr(Crypto.Random.random.randint(32, 127)) for i in range(16))
    return iv.encode('utf-8')


def file_encryption(file_name):
    f = open(file_name)
    f.close()
    aes_encryption(input_key(), f, f.name + ".aes")


def aes_encryption(key, f, enc_filename):
    """Short demonstration of AES-128 encrypting text files"""
    import os
    import struct
    import Crypto.Cipher.AES
    chunksize = 65536
    iv = generate_random_iv()
    print(sty.fg.green + "[+] " + sty.fg.rs + "iv:", iv)
    encryptor = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, iv)
    filesize = os.path.getsize(f.name)

    with open(f.name, 'rb') as infile:
        with open(enc_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            # struct.pack('<ii', long, long >> 32) is equivalent to '<q'
            outfile.write(iv)
            outfile.write(hash_methods.file_hash(f.name))

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk_padding = (' ' * (16 - len(chunk) % 16))
                    chunk_padding = str(chunk_padding).encode('utf-8')
                    chunk += chunk_padding

                outfile.write(encryptor.encrypt(chunk))
    print(sty.fg.green+"[+] "+sty.fg.rs+"File successfully encrypted")


def file_decryption(file_name):
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
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
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

            outfile.truncate(origsize)

        outfile_hash = hash_methods.file_hash(outfile.name)
        if outfile_hash == readed_hash:
            print(sty.fg.green + "[+] " + sty.fg.rs + "File successfully decrypted, hashes match\nhash:", outfile_hash)
        else:
            print(sty.fg.yellow + "[!] " + sty.fg.rs + "Hashes don't match")
            print(" - password is invalid, or")
            print(" - cipher text is damaged")
            print("readed hash                ", outfile_hash)
            print("passed hash of orginal file", readed_hash)
