def greeting(user:str, *y):
    print(f"Hello {user}. Welcome!")
# greeting("ali")
# greeting()


def add(*a):
    return sum(a)

def add_v2(*a):
    s = 0
    for x in a:
        s+=x
    return s


# print(add(1,20,30))
# print(add(1))
# print(add())
# print(10,20,30,40,50,60)

# x = (10,20,30,40,50,60)
# s = 0
# for i in x:
#     s+=i
# print(s)

# print(sum(x))
# ==========================================================
# 1,1,2,3,5,8,
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_v2(n):
    f = [1,1]
    for i in range(n-2):
        f.append(f[i]+f[i+1])
    return f[-1]

print(fib(6))
print(fib_v2(6))

f = [1,1]
n = int(input("Enter n:"))
for i in range(n-2):
    f.append(f[i]+f[i+1])
print(f)
print(f[-1])