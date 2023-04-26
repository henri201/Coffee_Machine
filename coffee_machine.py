from menu import MENU, resources
import os



profit = 0
def is_resource_sufficient(order_ingredience):
    


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
        is_resource_sufficient(drink["ingredience"])
