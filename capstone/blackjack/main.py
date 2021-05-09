############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## Create blackjack game
def blackjack():
    '''
    Starts a game of blackjack.
    '''
    print(logo)
    ## User receives two cards at the beginning
    your_cards = [random.choice(cards) for card in range(2)]
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

    ## Dealer receives one card at the beginning
    dealer_cards = [random.choice(cards) for card in range(2)]
    print(f"Dealer's first hand: {dealer_cards[0]}")

    ## while loop
    continue_drawing = True

    while continue_drawing:
        ## Ask user whether they want to draw a new card
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_input == 'y':
            your_cards.append(random.choice(cards))
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Dealer's first hand: {dealer_cards[0]}")
            ## Check if game is over: Blackjack or over 21 
            ## => if not ask again for input, else reveal dealer's cards
            if game_finished(your_cards):
                outcome = game_finished(your_cards)
                continue_drawing = False
        elif user_input == 'n':
            if sum(your_cards) <= 21:
                while sum(dealer_cards) <= 16:
                    dealer_cards.append(random.choice(cards))
            continue_drawing = False
    
    ### compare dealer_cards and your_cards
    if sum(your_cards) > 21:
        print_text(your_cards, dealer_cards)
        print(outcome)
    elif sum(dealer_cards) > 21:
        print_text(your_cards, dealer_cards)
        print(f"Opponent went over. You win.")
    elif sum(your_cards) > sum(dealer_cards) and sum(your_cards) == 21:
        print_text(your_cards, dealer_cards)
        print(outcome)
    elif sum(your_cards) > sum(dealer_cards):
        print_text(your_cards, dealer_cards)
        print("You win.")
    else:
        print_text(your_cards, dealer_cards)
        print("Dealer wins.")

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        #clear window
        print(chr(27) + "[2J")
        blackjack()

    return

## Automatic check whether game is over
def game_finished(current_hand):
    '''
    Checks automatically whether game is finished
    '''
    if sum(current_hand) > 21:
        ## check whether 11 is in current_hand > replace with one
        if 11 in current_hand:
            current_hand[current_hand.index(11)] = 1
        if sum(current_hand) > 21:
            return "You went over. You lose."
    if sum(current_hand) == 21:
        return "Blackjack. You win."
    else:
        return False

## Print text
def print_text(current_hand, opponent_hand):
    print(f"Your final hand: {current_hand}, final score: {sum(current_hand)}")
    print(f"Dealer's final hand: {opponent_hand}, final score: {sum(opponent_hand)}")


### Start a sequence
if __name__ == "__main__":
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        ### Clear window
        print(chr(27) + "[2J")
        blackjack()
