class car:
    def __init__(self, name="ford" , model=2002) :
        
        self.name=name
        self.model=model
    def sport(self):
            print("Sport car")

class sportcar(car):
    pass

c=sportcar("Sport car")
print(c.name)
print(c.model)
c.sport()