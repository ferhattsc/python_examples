n= int(input("enter the number:"))
if(n==1):
    print("it is not prime")
else:
    a=0
    for i in range(2,int((n/2))):
        if(n%i ==0):
            a=a+1
    if(a>1):
        print("it is not prime")
    else:
        print("it is prime ")