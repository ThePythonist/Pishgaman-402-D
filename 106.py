from random import randint


def generate1(length):
    password = []
    for i in range(length):
        digit = str(randint(0, 9))
        password.append(digit)

    password = "".join(password)
    print(password)


generate1(6)


def generate2(length):
    password = ""
    for i in range(length):
        digit = str(randint(0, 9))
        password += digit

    print(password)


generate2(6)
