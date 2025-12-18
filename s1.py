# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))
# flag = False
# if a>b and a>c:
#     if a**2 == b**2 + c**2:
#         print("قائم الزاویه است")
#         flag = True
# elif b>a and b>c:
#     if b**2 == a**2 + c**2:
#         print("قائم الزاویه است")
#         flag = True
# else:
#     if c**2 == b**2 + a**2:
#         print("قائم الزاویه است")
#         flag = True

# if flag == False:
#     print("قائم الزاویه نیست")


# counter = 3
# s = 0
# while counter>=1:
#     x = int(input("Enter a num:"))
#     s = s + x
#     counter = counter - 1
# print("sum=", s)


# y=int(input("n:"))
# counter =y
# s1=0
# s2=0
# while counter>=1:
#     x=int(input("enter num:"))
#     if x%2!=0:
#         s1= s1 + x
#     else:
#         s2=s2+x
    
#     counter = counter - 1
# print("sum1=", s1)
# print("sum2=", s2)


n = int(input("Enter n:"))
my_max = int(input("Enter a number:"))
my_min = my_max
c = 1
while c <= n-1:
    x = int(input("Enter a number:"))
    if x > my_max:
        my_max = x
    if x < my_min:
        my_min = x
    c = c + 1

print("max = " ,my_max)
print("min = " ,my_min)