from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:

    # User chooses drink
    user_choice = input(f"Which item do you want?: {menu.get_items()}: ")

    # Shows report of resources or finds drink from menu
    if user_choice == "report":
        coffee_maker.report()
    elif user_choice == "exit":
        machine_on = False
    elif menu.find_drink(user_choice) is not None:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
            money_machine.report()
        else:
            continue
