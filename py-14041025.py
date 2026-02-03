# number_list = [10,15,20,3,14,16,20,14,5,15]
# number_list.reverse()
# x = list(reversed(number_list))
# print(x)


# students = {
#     "name": "ali",
#     "grades": [15.25,10,20,19],
#     "math": 19.25,
#     "farsi": 18,
#     "grades1": {
#         "math": 15.25,
#         "sport" :10,
#     }
# }

# json

# unpack
# x,y,z = [10,20,30]
# print(x)
# print(y)
# print(z)

# x,*y,z = [10,20,30,40,50,60,70]
# print(x)
# print(y)
# print(z)

# ===================================================================
# n = int(input("Enter n:"))

# f = 1
# for i in range(1,n+1):
#     f *= i
# print(f"{n}! = {f}")


# ===================================================================
# function
def echo(name):
    print("Test:", name)

def add(x,y):
    print(x+y)

def add2(x,y):
    return x+y

z = add2(15,20)
# print(z)


def fact(m):
    f = 1
    for i in range(1,m+1):
        f *= i
    return f


# c(5,3)
x = fact(5)
y = fact(3)
z = fact(5-3)
# print(x/(y*z))


def operation(x,y,opt):
    if opt == '*':
        return x*y
    elif opt == '/':
        return x/y
    elif opt == '+':
        return x+y
    elif opt == '-':
        return x-y
    else:
        print("Wrong operator!")

# while True:
#     num1 = float(input("Enter 1st number:"))
#     num2 = float(input("Enter 2nd number:"))
#     # if num1==num2==0:
#     #     break
#     opt = input("Enter operator(*,/,+,-):")
#     res = operation(num1, num2, opt)
#     print(f"{num1} {opt} {num2} = {res}")
#     print('='*30)
#     c = int(input("Continue? 0: No - 1: Yes :"))
#     if c == 0:
#         break
#     print('='*30)
# operation(10,5,'*')
# operation(10,5,'/')
# operation(10,5,'-')
# operation(10,5,'+')


# ===================================================================
import random as rn
# print(rn.random())

# print(rn.randint(1,100))

# list_number = [10,20,3,100,40,200]
# print(rn.choice(list_number))

# print(rn.random()*100+10)

# ===================================================================
c = 1
while c<10:
    print(c)
    c +=1
    # if c > 5:
    #     break
else:
    print("Else")
print("Done")