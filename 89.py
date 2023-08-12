lines = open("words.txt").readlines()
sublst = []

for i in lines :
    if i[:3] == "sub":
        sublst.append(i)

print(sublst)
