from art import logo, vs
from game_data import data
import random

def start_game():
    a = random.choice(data)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    b = random.choice(data)
    ### test whether b equals a, if so assign new account to b
    while b == a:
        b = random.choice(data)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

    return a, b

def evaluate_game(a, b):
    if a['follower_count'] > b['follower_count']:
        return a, 'A', b
    elif a['follower_count'] < b['follower_count']:
        return b, 'B', a
    else:
        return None, None

def continue_game(celeb):
    print(logo)
    print(f"Compare A: {celeb['name']}, {celeb['description']}, from {celeb['country']}")
    print(vs)
    b = random.choice(data)
    ### test whether b equals a, if so assign new account to b
    while b == celeb:
        b = random.choice(data)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

    return celeb, b

if __name__ == '__main__':
    ##clear window
    print(chr(27) + "[2J")
    
    points = 0
    print(logo)
    a, b = start_game()
    continue_playing = True
    while continue_playing:
        more_followers, letter, less = evaluate_game(a, b)
        who_has_more = input("Who has more followers? Type 'A' or 'B': ").upper()
        if who_has_more == letter:
            points += 1
            ##clear window
            print(chr(27) + "[2J")

            print(f"You're right! {more_followers['name']} has {more_followers['follower_count']} followers. {less['name']} has {less['follower_count']} followers.")
            print(f"Current score: {points}. \n")
            a, b = continue_game(b)
        else:
            continue_playing = False

    print(f"Sorry, that is wrong. {more_followers['name']} has {more_followers['follower_count']} followers. {less['name']} has {less['follower_count']} followers.")
    print(f"Final score {points}.")
