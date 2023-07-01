# Coffee Machine OOP
# Munteanu Mihnea @ Mihnea03

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    request = ""

    while True:
        request = str(input("What coffee would you like to order? (espresso/latte/cappuccino): ")).lower()

        if request == 'quit':
            return

        if request == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(request)

            if drink is None:
                continue

            if drink.cost > money_machine.profit:
                if money_machine.make_payment(drink.cost) == True:
                    if coffee_maker.is_resource_sufficient(drink) == True:
                        coffee_maker.make_coffee(drink)
            else:
                if coffee_maker.is_resource_sufficient(drink) == True:
                    coffee_maker.make_coffee(drink)

if __name__ == '__main__':
    main()
