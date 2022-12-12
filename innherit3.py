class parent:
    parent_name=""
    child_nmae=""
    def parent(self):
        print("parent class")

class son(parent):
        def name(self):
            print("child name ")

class daughter(parent):
         def name(self):
            print("child name ")

s=son()
s.child_nmae=("I m son bob" )
s.parent()
print(s.child_nmae)

d=daughter()
d.child_nmae="I m daughter alexa"
d.parent()
print(d.child_nmae  )