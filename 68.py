# def number_status(number):
#     divs = [i for i in range(1, number + 1) if number % i == 0]
#     return "Prime" if len(divs) == 2 else "Composite"
#     # if len(divs) == 2:
#     #     return "Prime"
#     # else:
#     #     return "Composite"
#
#
# number = int(input("Enter any number : "))
# print(number_status(number))

def number_status(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    print("Prime") if len(divs) == 2 else print("Composite")
    # if len(divs) == 2:
    #     print("Prime")
    # else:
    #     print("Composite")


number = int(input("Enter any number : "))
number_status(number)
