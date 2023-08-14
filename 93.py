lines = open("words.txt", "r").read()
lines = lines.replace("\n", "")
open("oneline.txt", "w").write(lines)
print("Done")