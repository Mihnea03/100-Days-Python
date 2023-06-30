# Coffee Machine
# Munteanu Mihnea @ Mihnea03

import coffeem

def main():
    [water, milk, coffee, balance] = coffeem.init_quantities()

    request = ""
    while request != "quit":
        request = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

        if request not in coffeem.DRINKS and request != "report" and request != "refund" and request != "quit":
            print("Invalid request! Try again!")
        elif request == "refund":
            print(f"{round(balance, 2)}$ have been refunded!")
            balance = 0
        elif request == "report":
            coffeem.print_status(water, milk, coffee, balance)
        else:
            coffee_requirements = coffeem.DRINKS[request]

            if balance < coffee_requirements["price"]:
                print("Not enough balance!")
                balance = coffeem.add_to_balance(balance)

                if balance < coffee_requirements["price"]:
                    print(f"Not enough balance! {round(balance, 2)}$ have been refunded!")
                    balance = 0
            
            if balance >= coffee_requirements["price"]:
                if water < coffee_requirements["water"] or milk < coffee_requirements["milk"] or coffee < coffee_requirements["coffee"]:
                    print(f"Not enough resources. ${round(balance, 2)} have been refunded!")
                    balance = 0
                else:
                    water -= coffee_requirements["water"]
                    milk -= coffee_requirements["milk"]
                    coffee -= coffee_requirements["coffee"]
                    balance -= coffee_requirements["price"]

                    print(f"Here is your {request}! You have {round(balance, 2)}$ left.")

if __name__ == '__main__':
    main()