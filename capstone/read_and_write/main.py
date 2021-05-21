# Write to a file (using mode="w" to write to it, "a" to append to it)
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")

# Open the file (using with closes it at the end of the code block)
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Create new file
with open("new_file.txt", mode="w") as file:
    file.write("New text")