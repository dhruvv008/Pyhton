class parent:
    Dad=""
    Son=""
    def shoe_parent(self):
     print("parent class: ", self.Dad)

class son(parent):
        def son_method(self):
            print(self.Son, "Child:")

c=son()
c.Son="abc"
c.Dad="xyz"
print(c.Dad,c.Son)
c.shoe_parent()
c.son_method()