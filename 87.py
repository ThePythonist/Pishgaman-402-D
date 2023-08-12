# lines = open("words.txt").readlines()
# five_letters = ""
#
# for line in lines:
#     if len(line) == 6:
#         five_letters += line
#
# print(five_letters)
#
# open("fiveletters.txt", "w").write(five_letters)

lines = open("words.txt").readlines()
five_letters = []

for line in lines:
    if len(line) == 6:
        five_letters.append(line)

output = "".join(five_letters)

open("fiveletters.txt", "w").write(output)
