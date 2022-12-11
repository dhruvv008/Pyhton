def out():
    print("i m out")
    def IN():
        print("i m in ")
    IN()
out()      

print("--------------------------------")

def x():
    n1=int(input("Enter um10"))
    def y(n2):
        return n1*n2
    return y

m=x()
print(m(2))
