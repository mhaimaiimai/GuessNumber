import random
logo="""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|"""

EASY_LEVEL_TURN = 5
HARD_LEVEL_TURN = 10

def select_number():
    return random.randint(1,100)

def welcome():
    #logo
    print(logo)
    
    #welcome
    print(f"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {select_number()}""")

def set_difficulty():
    #difficulty
    difficulty = "" 
    while not (difficulty in ["easy","hard"]):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def compare(number, selected_number):
    if number > selected_number:
        print("Too high.")
    elif number < selected_number:
        print("Too low.")
    else:
        return True
    return False

def guessing(rem_guess):
    selected_number = select_number()
    for time in range(rem_guess):
        print(f"You have {rem_guess-time} attempts remaining to guess the number")
        number = int(input("Make a guess: "))
        is_correct = compare(number, selected_number)
        
        if is_correct:
            print(f"{number} is correct! You win!")
            break
        elif time == (rem_guess-1):
            print("You've run out of guesses, you lose")
            break
        else:
            print("Guess again.")

welcome()        
rem_guess= set_difficulty()
guessing(rem_guess)