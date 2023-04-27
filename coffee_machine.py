from menu import MENU, resources
import os



profit = 0

# check resources, looping through them and comparing, returns true when there is enough
def is_resource_sufficient(order_ingredience):
    for item in order_ingredience:
        if order_ingredience[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    # returns the total calculated from the coins inserted
    print("please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    #return true is payment is accepted, false if not
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry, thats not enough money.Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    #deduct the needed ingredients from the resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")

is_on = True

while is_on:
    current_resources = resources
    choice = input("what would you like? (espresso/latte/cappuchino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])