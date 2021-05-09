import random

def start_game():
    random_num = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_num:
            print("Too high.")
        elif guess < random_num:
            print("Too low.")
        else:
            return f"You got it. the answer was {guess}."
        attempts -= 1
        print("Guess again.")

    return "You run out of guesses, you lose."

if __name__ == '__main__':
    result = start_game()
    print(result)
    
