# -----------Get Average of numbers--------------
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

# -----------Get Average of grades--------------
# y=int(input("n:"))
# counter =1
# s = 0
# c = 0
# while counter<=y:
#     grade=float(input("enter grade:"))
#     unit = int(input("enter unit:"))
#     s = s + (grade * unit)
#     c = c + unit
#     counter = counter + 1

# print("avg=", s/c)
# print("sum=", s)
# print("unit=", c)

# -----------Get count of digits--------------
# 155468
# print(155468//10)
# x = int(input("Enter a number:"))
# count = 0
# while x != 0:
#     x = x // 10
#     count = count + 1
# print("count =", count)

# -----------Get sum of digits--------------
# x = int(input("Enter a number:"))
# s = 0
# while x != 0:
#     digit = x % 10
#     s = s + digit
#     x = x // 10
# print("sum =", s)

# -----------Get sum and count of odd and even digits--------------

x = int(input("Enter a number:"))
s_odd = 0
s_even = 0
c_odd = 0
c_even = 0
while x != 0:
    digit = x % 10
    if digit % 2 == 0:
        s_even = s_even + digit
        c_even = c_even + 1
    else:
        s_odd = s_odd + digit
        c_odd = c_odd + 1
    x = x // 10
print("sum of odd digits =", s_odd)
print("sum of even digits =", s_even)
print("count of odd digits =", c_odd)
print("count of even digits =", c_even)