n = int(input("enter set num"))
eng_students = set(list(map(int, input().split())))
print(eng_students)

b=int(input("enter set num"))
com_stud=set(list(map(int,input().split())))
print(b)

x=eng_students.symmetric_difference(com_stud)
print(x)
print(len(x))