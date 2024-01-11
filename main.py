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

money = 0.0
money = float("{:.2f}".format(money))
def print_report():

    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}')

def check_resource(drink):
    for item in MENU[drink]["ingredients"]:
        if (MENU[drink]["ingredients"][item] > resources[item]):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def check_money(drink, money):
    if (money < MENU[drink]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def get_money():
    print("Please insert coins.")
    quarter = int(input("how many quarters? "))
    dime = int(input("how many dimes? "))
    nickel = int(input("how many nickels? "))
    penny = int(input("how many pennies? "))
    money_rc =  quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    money_rc = "{:.2f}".format(money_rc)
    return float(money_rc)

def reduce_resource(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
# main menu - using case statement
    while (True):
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        match choice:
            case "report":
                print_report()
            case "off":
                break
            case "espresso" |"latte" |"capuccino": # multiple
                enough_resource = check_resource(choice)
                if (enough_resource):
                    money_rc = get_money()
                    enough_money = check_money(choice, money_rc)
                    if (enough_money):
                        reduce_resource(choice)
                        money += MENU[choice]["cost"]
                        print(f"Here is ${money_rc - MENU[choice]['cost']} in change.")
                        print(f"Here is your {choice} ☕️. Enjoy!")
            case _:
                print("Wrong choice. Try again !")
                pass


