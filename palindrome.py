string = input("Enter the string : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not")
