from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def PowerOn():
    order = input(f"What would you like? {menu.get_items()}: ")
    if order in admin_keywords:
        if order == "report":
            coffeemaker.report()
            moneymachine.report()
            PowerOn()
        else:
            return
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffeemaker.is_resource_sufficient(drink):
                print("$", drink.cost)
                moneymachine.make_payment(drink.cost)
                coffeemaker.make_coffee(drink)
                PowerOn()
        else:
            PowerOn()


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
admin_keywords = ["off", "report"]
PowerOn()