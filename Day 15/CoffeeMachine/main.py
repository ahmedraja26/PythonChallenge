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


# TODO : Prompt user by asking “What would you like?
def neworder():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order


# TODO : Off Prompt
# done in startMachine

# TODO: Print Report
def report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO: Check if resources are sufficient
def check_resources(water, milk, coffee, MENU, item):
    try:
        if water - MENU[item]['ingredients']['water'] < 0:
            print("Sorry there is not enough water.")
            return False
    except KeyError:
        pass
    try:
        if milk - MENU[item]['ingredients']['milk'] < 0:
            print("Sorry there is not enough milk.")
            return False
    except KeyError:
        pass
    try:
        if coffee - MENU[item]['ingredients']['coffee'] < 0:
            print("Sorry there is not enough coffee.")
            return False
    except KeyError:
        pass
    return True


# TODO: Process Coins
def process_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total


# TODO: Check Transaction successful
def enough_coin(total, MENU, item):
    if total - MENU[item]['cost'] < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


# TODO: Make Coffee
def make_coffee(water, milk, coffee, MENU, item, money):
    coffee = coffee
    milk = milk
    water = water
    try:
        water = water - MENU[item]['ingredients']['water']
    except KeyError:
        pass
    try:
        milk = milk - MENU[item]['ingredients']['milk']
    except KeyError:
        pass
    try:
        coffee = coffee - MENU[item]['ingredients']['coffee']
    except KeyError:
        pass
    try:
        money = money + MENU[item]['cost']
    except KeyError:
        pass
    return water, milk, coffee, money


def startMachine():
    machine_status_on = True
    water = 300
    milk = 200
    coffee = 100
    money = 0.00

    while machine_status_on:
        order = neworder()
        if order == "off":
            print("Machine Turned off")
            return
        elif order == "report":
            report(water, milk, coffee, money)
        elif order == "espresso":
            enough_resources = check_resources(water, milk, coffee, MENU, "espresso")
            if not enough_resources:
                continue
            total = process_coins()
            enough_money = enough_coin(total, MENU, "espresso")
            if not enough_money:
                continue
            else:
                print(f"Here is {total - MENU['latte']['cost']} dollars in change")
            water, milk, coffee, money = make_coffee(water, milk, coffee, MENU, "espresso", money)
            print("Here is your latte ☕. Enjoy!")
        elif order == "latte":
            enough_resources = check_resources(water, milk, coffee, MENU, "latte")
            if not enough_resources:
                continue
            total = process_coins()
            enough_money = enough_coin(total, MENU, "latte")
            if not enough_money:
                continue
            else:
                print(f"Here is {total - MENU['latte']['cost']} dollars in change")
                water, milk, coffee, money = make_coffee(water, milk, coffee, MENU, "latte", money)
            print("Here is your latte ☕. Enjoy!")
        elif order == "cappuccino":
            enough_resources = check_resources(water, milk, coffee, MENU, "cappuccino")
            if not enough_resources:
                continue
            total = process_coins()
            enough_money = enough_coin(total, MENU, "cappuccino")
            if not enough_money:
                continue
            else:
                print(f"Here is {total - MENU['cappuccino']['cost']} dollars in change")
            water, milk, coffee, money = make_coffee(water, milk, coffee, MENU, "cappuccino", money)
            print("Here is your latte ☕. Enjoy!")

        else:
            print("Invalid Input")


startMachine()
