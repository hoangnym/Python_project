#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Get names of guests and save in list
with open("Input/Names/invited_names.txt") as names:
    names = names.read().splitlines()

# Get content of letter
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        # write letter to each guest
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
            # replace [name] with name of guest
            new_letter.write(letter.replace("[name]", name))
        print(f"Letter ready for {name}.")


