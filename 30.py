a = 0
b = 1

for i in range(100):
    # c = a
    # a = b
    # b = b + c
    a, b = b, a + b
    print(a)

# while a < 100 :
#     print(a)
#     a, b = b, a + b
#
