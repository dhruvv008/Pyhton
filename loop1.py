num=1

while num <=100:
    print(num)
    num+=1


for i in  range(0,101):
    print("for loop" , i )


sum=0
num=int(input("ENter Number"))
for i in range(1,num+1):
    sum+=num
print(sum)

for i in "Hell Pyhton":
    if (i=="o"):
        break
    print("Charcater" , i)
