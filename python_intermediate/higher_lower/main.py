from art import logo, vs
from game_data import data
import random

def start_game():
    a = data[random.randint(0, len(data) - 1)]
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    b = data[random.randint(0, len(data) - 1)]
    ### test whether b equals a, if so assign new account to b
    while b == a:
        b = data[random.randint(0, len(data) - 1)]
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

    if a['follower_count'] > b['follower_count']:
        return a, 'A'
    elif a['follower_count'] < b['follower_count']:
        return b, 'B'
    else:
        return None, None

def continue_game(celeb):
    print(f"Compare A: {celeb.name}, {celeb.description}, from {celeb.country}")
    print(vs)
    b = data[random.randint(0, len(data) - 1)]
    ### test whether b equals a, if so assign new account to b
    while b == celeb:
        b = data[random.randint(0, len(data) - 1)]
    print(f"Compare B: {b.name}, {b.description}, from {b.country}")

    if celeb.follower_count > b.follower_count:
        return celeb, 'A'
    elif celeb.follower_count < b.follower_count:
        return b, 'B'
    else:
        return None, None

if __name__ == '__main__':
    points = 0
    print(logo)
    more_followers, letter = start_game()
    continue_playing = True
    while continue_playing:
        who_has_more = input("Who has more followers? Type 'A' or 'B': ").upper()
        if who_has_more == letter:
            points += 1
            print(f"You're right! Current score: {points}")
            more_followers, letter = continue_game(more_followers)
        else:
            continue_playing = False

    print(f"Sorry, that is wrong. Final score {points}.")
