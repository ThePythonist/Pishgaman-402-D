items = [10, 20, 10, 30, 20, 10, 40, 50]
unique_items = []

for i in items:
    if i not in unique_items:
        unique_items.append(i)

print(unique_items)
# print(list(set(items)))
