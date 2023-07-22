numbers = []

while True:
    entry = input("Type something : ")
    if entry == "exit":
        break
    else:
        try:
            entry = float(entry)
            if int(entry) == float(entry):
                numbers.append(int(entry))
            else:
                numbers.append(entry)
        except ValueError:
            print("Entry is not a number")

print(max(numbers))
