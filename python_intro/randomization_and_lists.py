#### Randomisation and Python Lists


####### Randomisation
import random
import my_module

# Create a random integer
random_int = random.randint(1, 10)
print(random_int)
print(my_module.pi)

# Create a random float number
random_float = random.random()
print(random_float * 5)

# Create a love score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")

# Create heads or tails game
heads_or_tails = random.random()
if heads_or_tails < 0.5:
    print("Heads")
else:
    print("Tails")


######### List
names = input("Who is going to pay the bill? Write all the names separated by a ','. \n").strip().split(",")
payee = names[random.randint(0, len(names) - 1)]

print(f"{payee} is going to pay today.")