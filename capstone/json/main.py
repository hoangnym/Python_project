# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# Catching Exceptions
# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)