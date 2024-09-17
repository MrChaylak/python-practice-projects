MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_check(user_choice, coffee_details, resources, enough_resources):
    water_left = resources["water"] - coffee_details["ingredients"]["water"]
    coffee_left = resources["coffee"] - coffee_details["ingredients"]["coffee"]
    if user_choice == "espresso":
        milk_left = resources["milk"]
    else:
        milk_left = resources["milk"] - coffee_details["ingredients"]["milk"]

    if water_left < 0:
        print("Sorry there is not enough water.")
        enough_resources = False
        return resources, enough_resources
    elif coffee_left < 0:
        print("Sorry there is not enough coffee.")
        enough_resources = False
        return resources, enough_resources
    elif user_choice != "espresso" and milk_left < 0:
        print("Sorry there is not enough milk.")
        enough_resources = False
        return resources, enough_resources
    else:
        return {
            "water": water_left,
            "milk": milk_left,
            "coffee": coffee_left
        }, enough_resources


def coins_checker(total_money, user_choice, coffee_details):
    print(f"Please insert coins, {user_choice} is ${coffee_details["cost"]}")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if coins < coffee_details["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        total_money += coffee_details["cost"]
        change = round(coins - coffee_details["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_choice}. Enjoy!")
    return total_money


total_money = 0
user_choice = ""

machine_on = True
while machine_on:
    enough_resources = True
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${total_money}")
    elif user_choice in MENU:
        coffee_details = MENU[user_choice]
        resources, enough_resources = resources_check(user_choice, coffee_details, resources, enough_resources)
        if enough_resources:
            total_money = coins_checker(total_money, user_choice, coffee_details)
    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")

print("Thank you for using Happy Coffee goods.")
