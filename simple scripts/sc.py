import re
file1 = open("2019.txt", errors='ignore')
file2 = open("ans.txt","w+")
for line in file1:
	if re.match("(.*)Ans(.*)", line):
		file2.write(line)

for lines in file2:
	if re.match(r"(.*)\((.*)\)", lines):
		file2.append(lines)
