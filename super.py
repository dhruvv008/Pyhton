class a:
    def fun(Self):
        print("I m super class ")

class b(a):
    def fun(Self):
        print(" i m child class")
        super().fun()

c=b()
c.fun()
