class car:
    model="Swidft"
    price=200000

c=car()
print(c.model ,c.price)    

class animal:
    name="Dogg"
    yr=5
    colour="BLack"

a=animal()
print(a.name)
print(a.colour)
print(a.yr)


class Class:
    def __init__(self, Fname, Roll) -> None:
        self.name=Fname
        self.no=Roll

c=Class("Dhurv", 2000)
c1=Class("urv", 2000)
c2=Class("v", 2000)
c3=Class("Dhv", 00)
c4=Class("D", 20)

print(c.name,c.no)
print(c1.name,c.no)
print(c2.name,c.no)
print(c3.name,c.no)
print(c4.name,c.no)
del c1.name
print(c1.name)
'''
print("new student")
a=input("ENter name : ")
b=int(input("ENter number"))
c=Class(a, b)
print(c.name,c.no)
'''
