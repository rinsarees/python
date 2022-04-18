from itertools import count


file = open("abc.txt","r")
Count = 0
Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Count += 1
          
print("Total number of lines in a text file is :")
print(Count)