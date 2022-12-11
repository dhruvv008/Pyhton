num=int(input("Enter Number :"))
a=0
b=1

if num>0:
    for i in range(2,num):
        c=a+b
        a,b=b,c
        
        print(c)
