length="Pyhton"
module="core python"
tmp="Three"

l=len(length)
m=len(module)
k=len(tmp)

print(l,m,k)

t=tmp.format(length=length, module=module)
print(t)

print(len(length))