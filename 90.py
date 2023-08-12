lines = open("words.txt").readlines()
inglst = []

for i in lines :
    # if i[-4:-1] == "ing":
    if "ing" in i[-4:]:
        inglst.append(i)

print(inglst)
