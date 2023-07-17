numbers = []

for i in range(3):
    entry = input("Entry : ")
    try:
        entry = float(entry)
        # if str(entry)[-2:] == ".0":
        if int(entry) == float(entry):
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        print("Entry is not a number")

print(numbers)
