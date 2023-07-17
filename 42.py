n = int(input("How many numbers do you need ? "))
nums = []

for i in range(n):
    x = int(input("Enter a number : "))
    nums.append(x)

print(max(nums))
