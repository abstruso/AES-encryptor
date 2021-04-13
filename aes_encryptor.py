#!/usr/bin/env python3
import number_field_arithmetic
import aes_methods
import hash_methods


def main():
    print("What can I do for you?\n")
    print_menu_options()

    while True:
        selector = input("Choose option ")

        if selector == "1":
            number_field_arithmetic.modulus_aritmetic(number_field_arithmetic.choose_prime())
            come_back_to_menu()
            continue
        if selector == "2":
            file_name = hash_methods.get_file()
            print(hash_methods.file_hash(file_name))
            come_back_to_menu()
            continue
        if selector == "3":
            aes_methods.aes_demonstration()
            come_back_to_menu()
        if selector == "4":
            file_name = hash_methods.get_file()
            aes_methods.file_encryption(file_name)
            come_back_to_menu()
        if selector == "5":
            file_name = hash_methods.get_file()
            aes_methods.file_decryption(file_name)
            come_back_to_menu()
        if selector == "6":
            exit()
        else:
            print("there isn't such function")


def come_back_to_menu():
    print("\nDo you want to exit program? y/n")
    command = input()
    if command.endswith("y"):
        exit()
    else:
        main()


def print_menu_options():
    print("[1] Number field aritmetic")
    print("[2] SHA256 Hash function of specified file")
    print("[3] AES-128 encryption and decryption demonstration")
    print("[4] Encrypt file with AES-128")
    print("[5] Decrypt file with AES-128")
    print("[6] Exit")


if __name__ == '__main__':
    main()
