from menu import MENU, resources
import os

is_on = True

while is_on:
    choice = input("what would you like? (espresso/latte/cappuchino): ")
    if choice == "off":
        is_on = False