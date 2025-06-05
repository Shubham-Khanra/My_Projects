import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors.\n'))


# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])



# computer's choice logic:

computer_choice = random.randint(0,2)
print('Computer chose:')
print(game_images[computer_choice])


# Game Rule's Logic:

if user_choice >=3 or user_choice < 0:
    print('You have made an invalid choice! Game Over!!!')

elif user_choice == 0 and computer_choice == 2:
    print('You Won!')

elif user_choice == 2 and computer_choice == 0:
    print('You Lose!')

elif user_choice > computer_choice:
    print('You Lose!')

elif computer_choice > user_choice:
    print('You Won!')

elif computer_choice == user_choice:
    print("It's a Draw!")