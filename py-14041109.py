# Menu
# 1: Check prime number
# 2: Check complete(Perfect) number
# 3: Check Factorial number
# 4: Positive or negative number
# 5: Cal number digits 
# 6: Cal sum of number digits
# 0: exit

def prime_number(x):
    pass

def complete_number(x):
    pass

def fact(x):
    pass

def sign_number(x):
    pass

def number_digit(x):
    pass

def sum_digit(x):
    s = 0
    while x != 0:
        s += x%10
        x //=10
    print("Sum of digits:", s)

def score_list():
    x = {
        'names': [],
        'units': [1,2,2,3],
        'grades': [15,16,20,18.5]
    }

def menu():
    while True:
        print("="*30)
        print('''
        1: Check prime number
        2: Check complete(Perfect) number
        3: Check Factorial number
        4: Positive or negative number
        5: Cal number digits 
        6: Cal sum of number digits
        7: Get score list
        0: exit
        ''')
        
        ch = int(input("Enter your choice:"))
        if ch == 0:
            break
        elif ch == 7:
            score_list()
        x = int(input("Enter your number:"))
        if ch == 1:
            prime_number(x)
        elif ch == 2:
            complete_number(x)
        elif ch == 3:
            fact(x)
        elif ch == 4:
            sign_number(x)
        elif ch == 5:
            number_digit(x)
        elif ch == 6:
            sum_digit(x)
        else:
            print("Wrong option.Try again!")

        c = input("Press Enter to continue...")
    
# menu()
# x = {
#     'names': [],
#     'units': [1,2,2,3],
#     'grades': [15,16,20,18.5]
# }

# print(x["key10"])
# print(x.get("key10"))

# print(x.popitem())

# x.update(key3=15.5)
# x.update({'key4': [1,2,3,4]})
# print(x)

# print(x.get('units').append(10))

# y = x.get('units')
# y.append(10)
# x.update({'units': y})
# print(x)





try:
    x = int(input("Enter x:"))
except ValueError:
    print("Wrong input! ValueError")
except IndexError:
    print("Wrong input! IndexError")
except:
    pass
# print(x)