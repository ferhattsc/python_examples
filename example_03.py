from re import L


l=[]
for i in range(3):
    n=int(input("Enter number: "))
    l.append(n)
big=0
for i in l:
    if i>big:
        big=i;
print("The biggest number:",big)
