nums = []
for i in range(5):
    x = int(input("Enter any number :"))
    nums.append(x)

nums.sort()
print(nums[::-1])
