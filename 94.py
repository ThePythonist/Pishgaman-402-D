# lines = open("words.txt").readlines()
# lines = lines[::-1]
# output = "".join(lines)
# open("reverse.txt","w").write(output)


lines = open("words.txt").readlines()
rev_lines = []

for line in lines :
	rev_lines.append(line[::-1])

output = "".join(rev_lines)
open("reverse.txt","w").write(output)
