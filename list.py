list=[1,1,2,3,5,8,13,21,34,55,89]
 
new_list= [ ]
  
print(list)

for element in list :

    if element < 5 :
        new_list .append(element)

print("The list of numbers that are less than 5:", new_list)