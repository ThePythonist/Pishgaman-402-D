from random import randint, choice

start = int(input("Start range : "))
end = int(input("End range : "))

# print(randint(start, end))
print(choice(range(start, end)))
