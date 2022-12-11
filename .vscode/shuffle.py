import random

list=["a","b","c","d","e","f","g","h",]

list2=["a1","b2","c3","d4","e5","f5","g6","h7",]
print(list)

random.shuffle(list)
print(list)

merge=[]
merge=list+list2
print(merge)

merge.extend(list2)
print(merge)