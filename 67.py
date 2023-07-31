def filter(items):
    numbers = []

    for i in items:
        if type(i) in [int, float]:
            numbers.append(i)
    return numbers


items = [True, 12, 4, 6.5, "Python", 11]
print(filter(items))
