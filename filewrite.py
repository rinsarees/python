a_list = ["Rinsa", "Johnson", "Steve"]
textfile = open("abc.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()
