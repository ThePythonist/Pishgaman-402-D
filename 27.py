flag = True

while flag:
    entry = input("Type something : ")
    print(entry)
    if entry == "exit":
        # flag = False
        break
else:
    print("Flag has turned into false")
