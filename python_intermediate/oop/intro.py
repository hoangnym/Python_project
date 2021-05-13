# from turtle import Turtle, Screen
# # TK_SILENCE_DEPRECATION = 1
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


from prettytable import PrettyTable

pokedex = PrettyTable()
pokedex.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokedex.add_column("Type", ["Electro", "Water", "Fire"])
pokedex.align = "l"

print(pokedex)