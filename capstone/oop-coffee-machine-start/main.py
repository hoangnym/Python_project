from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

taking_order = True

while taking_order:
    # Ask user for order
    order = input("What would you like to drink? (espresso, latte, cappuccino): ")

    # Print report
    if order == "report":
        coffee_maker.report()

    elif order == "off":
        taking_order = False

    else:
        # Check resources sufficient?
        menu_item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(menu_item):
            print(menu_item)
            # Process coins and check transaction successful
            if money_machine.make_payment(menu_item.cost):
                # Make coffee
                coffee_maker.make_coffee(menu_item)