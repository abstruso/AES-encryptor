def is_prime(number):
    """
    Check if given number is prime
    :returns True, False
    """
    import math
    if number == 0 or number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def choose_prime():
    import Crypto.Util.number

    print("Please choose your prime base by direct specification or generation")
    number = input("a) specified prime (leave blank for 7): ")
    if number == "":
        prime = 7

    else:
        while not is_prime(int(number)):
            print(number, "is not a prime")
            number = input("try again ")

    if number != "":
        prime = number
        prime = int(prime)
        return prime

    bits = input("b) number of bits (ec 1024) ")

    if bits != "":
        print("Number of bits in prime p is", bits)
        prime = int(Crypto.Util.number.getPrime(int(bits)))
        print("\nRandom n-bit Prime (p): ", prime)

    return prime


def modulus_aritmetic(prime):
    """First, most basic element of our program. Does simple operations read form natural notation."""
    print("your p = ", prime)
    print("\nPlease enter statement to be calculated in modulo p," +
          "for example 45242+52435 (only two arguments), or one argument with # " +
          "to calculate reverse element in mod p body for example 3#")

    statement = input()

    if "#" in statement:
        calculate_reverse_element(statement, prime)
    else:
        modulus_aritmetic_operations(statement, prime)


def modulus_aritmetic_operations(statement, prime):
    if "+" in statement:
        arguments = statement.split('+')

        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        result = arguments[0] + arguments[1]
        result %= prime
        print(result)

    if "-" in statement:
        arguments = statement.split('-')

        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        result = arguments[0] - arguments[1]
        result %= prime
        print(result)

    if "*" in statement:
        arguments = statement.split('*')

        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        result = arguments[0] * arguments[1]
        result %= prime
        print(result)


def calculate_reverse_element(statement, p):
    """Calculate reverse element in mod p body."""
    arguments = statement.split('#')
    a = int(arguments[0])
    # reverse element will exists for because p is prime and gcd(a,p)==1
    result = gcd_extended(a, p)[1]
    if result < 0:
        result = p + result
    print(result)


def gcd_extended(a, b):
    """Extended Euclidean algorithm"""
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
