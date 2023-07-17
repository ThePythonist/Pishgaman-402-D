pythons = ["ali", "hamid", "zahra", "farzad"]
icdls = ["ali", "pedram", "tara", "mina", "zahra"]
common = []

# for i in pythons:
#     if i in icdls:
#         common.append(i)
#
# print(common)


for i in pythons:  # 4
    for j in icdls:  # 5
        if i == j:  # 20
            common.append(i)

print(common)
