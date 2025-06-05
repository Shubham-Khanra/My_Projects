import random
import time

# This function prints out text with a small delay giving a typing effect.
def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(0.05)
    print('\n')
    

# this will be our function for game.
def game():
    #choices for our game
    choices = ['rock', 'paper', 'scissor']

    
    # we print the rule of the game for the newcomers and also display a welcome message.
    print_slow("welcome to the classic gane -- Rock, paper and scissor.")
    print_slow('The rules are simple: \nRock crushes scissor, scissor cuts paper and Paper wraps Rock')
    print_slow('Let\s start the game...')
    
    
    # The game will continue to a loop until the player decides to stop it.
    
    while True:
        print_slow('Please enter your choice(rock / paper / scissor)')
        player_choice = input().lower()
        
        # we check if user's choice is valid and from the list of choices.
        if player_choice not in choices:
            print_slow('Invalid Choice. Please choose between rock, paper or scissor.')
            continue
        
        print_slow('You chose '+ player_choice + '. Now it\'s my turn')
        time.sleep(1)
    
    
        # Now the computer will make a choice from the choice list.
        computer_choice = random.choice(choices)
        print_slow('I chose ' + computer_choice + '.')

        
        # Determine the winner of this game.
        if player_choice == computer_choice:
            print_slow('It is a tie!')
        elif(player_choice == 'rock' and computer_choice == 'scissor') or \
            (player_choice == 'scissor' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):
            print_slow('You win!')
        else:
            print_slow('I win!')
        
        # We now ask whether the user wants to play again.
        print_slow('Do you want to play again? (yes/no)')
        play_again = input().lower()
        
        if play_again != 'yes':
            break

# Now we will implement the final portion of our game which in the game finction that will run when the script is excecuted.

if __name__ == '__main__':
    game()
