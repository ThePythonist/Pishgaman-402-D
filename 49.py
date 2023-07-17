number = int(input("Enter any number : "))

# divs = []
divs = list()

for i in range(1, number + 1):
    if number % i == 0:
        divs.append(i)

# divs = [ i for i in range(1,number+1) if number % i == 0]

print(divs)

if len(divs) == 2:
    print("Prime")
else:
    print("Not Prime")

# ------------------------------------------------------------------

# number = int(input("Enter any number : "))
# divs = 0
#
# for i in range(1, number + 1):
#     if number % i == 0:
#         divs += 1
#
# if divs > 2:
#     print("Not Prime")
# else:
#     print("Prime")
