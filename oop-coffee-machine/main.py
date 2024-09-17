from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()
machine_on = True
while machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").strip().lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice):
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Pick a coffee from the list please.")
print("Machine is off.")
