import random
from replit import clear
from artguessnumber import logo

play = True
def game():
    def difficulty_choice():
        if difficulty.lower() == "easy":
            return 10
        else:
            return 5
        
        
    def guess_portion():
        if player_guess == my_num:
            return 2
        elif player_guess < my_num:
            return 1
        else:
            return 0
            
            
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")
    player_life = difficulty_choice()
    my_num = random.randint(1, 100)
    while player_life > 0:
        print(f"you have {player_life} attempts remaining to guess the number. ")
        player_guess = int(input("make a guess: "))
        answer_value = guess_portion()
        if answer_value == 2:
            print(f'you got it! The answer was {my_num}')
            player_life = 0
        elif answer_value == 1:
            print("Too low")
            player_life -= 1
        else:
            print("Too high")
            player_life -= 1
    
while play:
    print(logo)
    game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'n':
        play = False
    else:
        clear()
