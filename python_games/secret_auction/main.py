from art import logo

print(logo)

# Create empty dictionary
biddings = {}

keep_bidding = True

while keep_bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid? €")

    biddings[name] = bid

    additional = input("Are there other users who want to bid (yes / no)?: ").lower()

    if additional == "no":
        keep_bidding = False

    #Clear window
    print(chr(27) + "[2J")


amount = max(biddings.values())
highest_bidder = [k for k, v in biddings.items() if v == amount][0]

print(f"{highest_bidder} wins the secret auction with a bid of {amount}.")
