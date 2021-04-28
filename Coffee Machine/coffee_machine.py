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
    "money": 0,
}


def available_ressource(order):
    not_enough = []
    for k, v in MENU[order]["ingredients"].items():
        if v > resources[k]:
            not_enough.append(k)
    return not_enough


def ask_coins():
    print("Please insert coins.")
    total = 0
    total += (int(input("How many quarters? ")) * 0.25)
    total += (int(input("How many dimes? ")) * 0.10)    
    total += (int(input("How many nickles? ")) * 0.05)    
    total += (int(input("How many pennies? ")) * 0.01)        
    return round(total, 2)


def return_change(drink_cost, money_given):
    """Returns the difference and increments the treasury"""
    print(f"You inserted ${money_given}")
    resources["money"] += drink_cost
    if money_given > drink_cost:
        change = money_given - drink_cost
        print(f"Here is {round(change, 2)} in change.")


def brew_drink(order):
    """decrements the resources upon brewing a drink"""
    for k, v in MENU[order]["ingredients"].items():
        resources[k] -= v


def report():
    for k, v in resources.items():
        print(f"{k}: {v}")


def coffee_machine():
    drink_keywords = ["espresso", "latte", "cappuccino"]
    admin_keywords = ["off", "report"]
    lacking_resources = []
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in drink_keywords:
        lacking_resources = available_ressource(order)
        if not lacking_resources:
            drink_cost = MENU[order]['cost']
            print('$', drink_cost)
            total_given = ask_coins()
            if total_given >= drink_cost:
                return_change(drink_cost, total_given)
                brew_drink(order)
                print(f"Here is you {order}. Enjoy!")
                coffee_machine()
            else:
                print("Sorry, that's not enough money. Money refunded.")
                coffee_machine()
        else:
            for i in lacking_resources:
                print(f"Not enough {i}")
            coffee_machine()
    elif order in admin_keywords:
        if order == "report":
            report()
            coffee_machine()
        else:
            return
    else:
        print("Input Error...")
        coffee_machine()


coffee_machine()
