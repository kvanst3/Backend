from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def PowerOn():
    order = input(f"What would you like? {menu.get_items()}: ")
    if order in admin_keywords:
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            return
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                print("$", drink.cost)
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
    PowerOn()


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
admin_keywords = ["off", "report"]
PowerOn()
