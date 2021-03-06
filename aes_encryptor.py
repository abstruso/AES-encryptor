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
            case_1()
        if selector == "2":
            case_2()
        if selector == "3":
            case_3()
        if selector == "4":
            case_4()
        if selector == "5":
            case_5()
        if selector == "6":
            exit()
        else:
            print("there isn't such function")


def case_1():
    number_field_arithmetic.modulus_aritmetic(number_field_arithmetic.choose_prime())
    come_back_to_menu()


def case_2():
    file_name = hash_methods.get_file()
    print(hash_methods.file_hash(file_name))
    come_back_to_menu()


def case_3():
    aes_methods.aes_demonstration()
    come_back_to_menu()


def case_4():
    file_name = hash_methods.get_file()
    aes_methods.file_encryption(file_name)
    come_back_to_menu()


def case_5():
    file_name = hash_methods.get_file()
    aes_methods.file_decryption(file_name)
    come_back_to_menu()


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
