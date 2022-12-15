class father:
    def __init__(self,fathername ,fatherage) :
        self.name=fathername
        self.age=fatherage
        
    ''' def details(self):
        print(" Father " ,self.name,self.age)
'''
class mother:
    def __init__(self,mothername,motherage) :
        self.aname=mothername
        self.bage=motherage

    '''def detailsmother(self):
        print(" mother " ,self.aname,self.bage)
'''
class son(father,mother):
    def __init__(self, name,age ,aname,bage ):
        father.__init__(self,name,age)
        mother.__init__(self,aname,bage)


s=son("Abc",50,"xyz",45)
'''
s.details()

s.detailsmother()'''

print("Daddy",s.age,s.name)
print("mommy", s.aname,s.bage)