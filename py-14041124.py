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

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

# 5*4 = 5+5+5+5
def mul(n,m):
    if m==1:
        return n
    return n + mul(n,m-1)


def div(n,m):
    if n < m:
        return 0
    return 1 + div(n-m, m)


# print(fib(6))
# print(fib_v2(6))

# ==================================================================
# Files
f = open("files/numbers.txt")
# print(f.read(5))
# print(f.read(5))
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readlines())

s = "  hello  hi   \n"
s2 = s.strip()
print(s2)