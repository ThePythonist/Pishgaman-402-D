items = [
    3.5,
    "tehran",
    "tokyo",
    38,
    25,
    12.3,
    "paris",
    23,
    "london",
    21
]

numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
