a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

print("First list ", a)
print("Second list ", b)
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
c=set(c)
print("The elements that are common between the lists ", c)