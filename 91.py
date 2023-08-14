# lines = open("words.txt", "r").readlines()
# new_lines = []
#
# for i in lines :
#     new_lines.append(i[:-1])
#
# print(new_lines[:100])

# --------------------------------------------
lines = open("words.txt", "r").read()
print(lines.split("\n"))
