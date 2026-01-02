# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# for i in range(10,0,-1):
#     print(i)

# --------------------------------
# n = int(input("Enter n:"))
# s = 0
# for i in range(n):
#     x = int(input("Enter your number:"))
#     s += x
# print("sum =", s)
# ----------------------------
# start = int(input("Enter start:"))
# stop= int(input("Enter stop:"))
# s = 0
# for i in range(start, stop+1):
#     s += i
# print(s)

# ----------------------------
# for x in range(1,10):
#     for y in range(0,10):
#         print(x,y)


# for i in [1,5,16,17,18]:
#     print(i)

# x = 10
# str(x) -> '10'

# x = '10'
# int(x) -> 10
# float(x) -> 10.0


# -----------------------------------------
# List
x = 'hello'
number_list = [10,20,30,40, 'hello', 10.25]
# print(number_list[-6])
# number_list[3] = 1000
# print(len(number_list))
# print(number_list[::-1])

# num = []
# num = list()

# List methods
# number_list.append(100)
# print(number_list)
# number_list.insert(2,400)
# print(number_list)

# userinp = int(input("tedade baze: "))
# numList = []
# s = 0
# for i in range(userinp):
#     adad = int(input("adade list: "))
#     numList.append(adad)
#     s += adad
# print(numList)
# print("sum =", s)


# ------------------------------------
# number_list = [11,20,31,40,50,60,7]
# for x in number_list:
#     if x % 2 == 0:
#         print(x*2)
#     else:
#         print(x**2)

# for i in range(len(number_list)):
#     print(number_list[i])
# s = 0
# for i , x in enumerate(number_list):
#     print("index:",i, " Value:",x)
#     s += x
# print("Sum:", s)
# print("Sum:", sum(number_list))
# -----------------------------------
# Min and Max
number_list = [11,20,31,40,50,60,7]
# min_value = number_list[0]
# max_value = number_list[0]
# for x in number_list:
#     if x < min_value:
#         min_value = x
#     if x > max_value:
#         max_value = x
# print("Min:", min_value)
# print("Min:", min(number_list))
# print("Max:", max_value)
# print("Max:", max(number_list))

x = number_list.pop()
x = number_list.pop(2)
number_list.remove(11)

if x in number_list:
    number_list.remove(x)

number_list.count(7)
number_list.index(11)
