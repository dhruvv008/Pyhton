dict={
    "Student:":"abc",
    "Roll no":2121
}
dict.pop('Roll no')
print(dict)

list=[]
for i in dict:
    b=(i,dict[i])
    list.append(b)
    print(list)

