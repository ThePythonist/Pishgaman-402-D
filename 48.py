number = 12
divs = []

for i in range(1, number + 1):
    if number % i == 0:
        divs.append(i)

print(divs)