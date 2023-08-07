integer = 10
decimal = int(input("Enter decimal part : "))
# number = f"{integer}.{decimal}"
number = "{i}.{d}".format(i=integer, d=decimal)
number = float(number)
print(number)
