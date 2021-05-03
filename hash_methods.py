def get_file():
    """User chooses file to proceed"""
    import os
    import sty
    print("Now we are in:", os.path.dirname(os.path.realpath(__file__)))
    file_details = input("Path to file, or filename if file in this directory: ")
    if file_check(file_details):
        return file_details
    else:
        print(sty.fg.yellow + "[!] " + sty.fg.rs + "Try again")
        file_details = input()
        if file_check(file_details):
            return file_details
        else:
            exit()


def file_hash(file_name):
    """Returns SHA256 hash of file with given name"""
    import Crypto.Hash.SHA256
    hasher = Crypto.Hash.SHA256.new()
    chunk_size = 65536
    with open(file_name, "rb") as file:
        while True:
            data = file.read(chunk_size)
            hasher.update(data)
            if not data:
                break
    return hasher.hexdigest().encode('utf-8')


def file_check(file_details):
    """Check if file can be open"""
    import sty
    try:
        open(file_details, "r")
    except IOError:
        print(sty.fg.yellow + "[!] " + sty.fg.rs + "File can't be open")
        return False
    return True
