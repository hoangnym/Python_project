import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
# Use a while loop to let the user guess again
end_of_game = False

#Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

# print logo
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = ['_' for letter in chosen_word]
print(display)

#Create empty array of guessed letters
guessed = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If user guessed a letter already guessed, let user know, print checked letter
    if guess in guessed:
        print(f"You already guessed {guess}.")
        lives += 1
    else:
        guessed.append(guess)

    #Loop through each position in the chosen_word;
    for i in range(len(chosen_word)):
        #print(f"Current position: {i}\n Current letter: {chosen_word[i]}\n Guessed letter: {guess}")
        if guess == chosen_word[i]:
            display[i] = guess

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. \n We looked for {chosen_word}." )


    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(hangman_art.stages[lives])
    print(display)
    print(f"Already used {guessed}")

    #Check if '_' in display => if not, end_of_game = True
    if '_' not in display:
        end_of_game = True
        print("You win.")
