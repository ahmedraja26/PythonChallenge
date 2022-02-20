from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()

machineRunning = True
while machineRunning:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        machineRunning = False
    elif order == "report":
        print(f"{coffeeMachine.report()}")
        print(f"{moneyMachine.report()}")
    elif menu.find_drink(order) is not None:
        item = menu.find_drink(order)
        haveResources = coffeeMachine.is_resource_sufficient(item)
        if haveResources:
            sufficientMoney = moneyMachine.make_payment(item.cost)
            if not sufficientMoney:
                continue
            else:
                coffeeMachine.make_coffee(item)
        else:
            continue
