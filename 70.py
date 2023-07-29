def numberstatus(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


def checknumber(x):
    if type(x) in [int, float]:
        print("X is a number :")
        print(numberstatus(x))
    else:
        print("X is not a number")


checknumber(44)
