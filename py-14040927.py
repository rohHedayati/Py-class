# y=int(input("n:"))
# counter =1
# s1 = 0
# s2 = 0
# c1 = 0
# c2 = 0
# while counter<=y:
#     x=int(input("enter num:"))
#     if x%2!=0:
#         s1= s1 + x
#         c1 = c1 + 1
#     else:
#         s2=s2+x
#         c2 = c2 + 1
    
#     counter = counter + 1
# print("avg1=", s1/c1)
# print("avg2=", s2/c2)

y=int(input("n:"))
counter =1
s = 0
c = 0
while counter<=y:
    grade=float(input("enter grade:"))
    unit = int(input("enter unit:"))
    s = s + (grade * unit)
    c = c + unit
    counter = counter + 1

print("avg=", s/c)
print("sum=", s)
print("unit=", c)
