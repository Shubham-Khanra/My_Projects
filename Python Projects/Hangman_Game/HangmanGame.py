# importing modules
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list).lower()
print(chosen_word)
hangman_lives = 6 # no of times to guess correct letter


# replace the chosen_word by '_' for each letter

placeholder  = ''

for position in range(len(chosen_word)):
    placeholder += '_'
print('Word to guess: ' + placeholder)



# Task:1 If the letter at that position matches guess then reveal that letter in the display at that position.
# Task:2 Taking input until the game is not over which means all '_' are replaced by letters.
# Task:3 Keep storing the previous letter taken from user.

game_over = False
correct_letters = []

while not game_over:
    
    # Task:7 Update the code below to tell the user how many lives they have left.
    print(f"****************************{hangman_lives}/6 LIVES LEFT****************************")
    guess = input('guess a letter: ').lower() # user input for correct letter.
    
    
    # Task:8 If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in chosen_word:
        print(f'you have already entered {guess}')
    
    
    
    display = ''    # To store the guessed letter and blanks.
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        
        elif letter in correct_letters:
            display += letter
        
        else:
            display += '_'
    print(display)

    
    # Task:4 If there is no blanks (_), then on screen it will be shown 'You Win'  
  
    if '_' not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    # Task:5 Adding limitations to guess the correct letter.  
      
    if guess not in chosen_word:
        hangman_lives -= 1
        
        if hangman_lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            


    # Task:6 print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[hangman_lives])