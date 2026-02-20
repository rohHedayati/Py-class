numbers = [10,2,3,4,5,6]
new_numbers = []
for x in numbers:
    if x % 2 == 0:
        new_numbers.append(x**2)
# print(new_numbers)

# new_list = [x**2 for x in numbers if x%2==0]
new_list = [x**2 if x%2==0 else x*2 for x in numbers]
print(new_list)