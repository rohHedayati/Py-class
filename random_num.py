import random

random_num = random.randint(1,100)
try_count = 0

while try_count<5:
    x = int(input("Enter your choice:"))
    try_count += 1
    if x == random_num:
        print(f"You win, your choice:{x} - computer: {random_num}")
        print("Total try:", try_count)
        break
    elif x > random_num:
        print("choice smaller number!")
    else:
        print("choice larger number!")
else:
    print("You Lose")