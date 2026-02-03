def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

# n = int(input("Enter your number:"))
# c = 0
# for i in range(1,n+1):      
#     if is_prime(i):
#         c += 1
#         print(i, "is a prime number")            
# print("Total prime numbers:", c)   
                                               


# n=5
# *
# **
# ***
# ****
# *****
n = int(input("Enter n:"))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n,0,-1):
#     print("*"*i)

# n=5
#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,n+1):
#     msg = " "*(n-i)
#     msg += "*"*i
#     print(msg)

# n=5
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1,n+1):
    msg = " "*(n-i)
    msg += "*"*(2*i-1)
    print(msg)