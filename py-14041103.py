import random as rnd

def compare_choices(user, computer):
    global user_score
    global computer_score
    if (user == computer):
        pass
    elif (user == 0 and computer == 1) or \
        (user == 1 and computer == 2) or \
        (user == 2 and computer == 0):
        user_score += 1
    elif (user == 0 and computer == 2) or \
        (user == 1 and computer == 0) or \
        (user == 2 and computer == 1):
        computer_score += 1

def get_user_choice():
    print("Enter 0 : For Rock")
    print("Enter 1 : For Scissor")
    print("Enter 2 : For Paper")
    user_choice = int(input("Enter your choice:"))
    return user_choice

user_score = 0
computer_score = 0
Rounds = 0
choices = [0, 1, 2]

while True:
    user_choice = get_user_choice()
    computer_choice = rnd.choice(choices)
    print("Computer choice:", computer_choice)

    Rounds += 1
    compare_choices(user_choice, computer_choice)
    
    print("="*30)
    print(f"User score: {user_score}  --- Computer score: {computer_score}")
    print("="*30)

    if Rounds >= 5 :
        break

if user_score > computer_score:
    print("User win the game!")
elif user_score < computer_score:
    print("Computer win the game!")
else:
    print("Equal!")