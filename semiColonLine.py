file1 = open("filename.txt", "r")
file2 = open("player.txt", "w+")
for line in file1:
	words = line.split(" ")
	for word in words:
                for letter in word:
                        if(letter ==';'):
                                 file2.write(letter)
                                 file2.write("\n")                               
                        else:
                                file2.write(letter)

file1.close()
file2.close()
			
			
