class father:
    def fatherfun(self):
        print(" I m Dad fumctiom")

class mother (father):
    def motherfun(self):
        print(" i m  Mother ")

class son(mother):
    def sonfun(self):
        print(" i m son")

s=son()
s.sonfun()
s.motherfun()
s.fatherfun()
