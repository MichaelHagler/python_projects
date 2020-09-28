import random

def d6():
    print(random.randint(1, 6))

def d10():
    print(random.randint(1, 10))

def d20():
    print(random.randint(1, 20))


roll_again = input('do you want to roll? yes or no? ')
if roll_again == 'no':
    print("Thanks for using dice roller.")

while roll_again == 'yes':

    dice = input("pick a die; 6, 10, 20: ")
    if dice == str('6'):
        d6()
    elif dice == str('10'):
        d10()
    else:
        d20()
    roll_again = input('do you want to roll again? yes or no? ')

    if roll_again == 'no':
        print("Thanks for using dice roller.")
