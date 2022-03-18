number = int(input("Enter the number: "))
print("\nDivisor of %d are:  " %(number))
for i in range(1,number+1):
    if number %i == 0:
        print(i,end=" ")


