fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"The index {index} is out of range.")
    else:
        print(fruit + " pie")


make_pie(4)