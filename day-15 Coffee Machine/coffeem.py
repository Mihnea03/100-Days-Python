# Coffee Machine
# Munteanu Mihnea @ Mihnea03

WATER_Q = 300
MILK_Q = 200
COFFEE_Q = 100

DRINKS = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.5
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 2.5
    }
}

CURRENCY = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

PRINT_STATUS_FORMAT = """Water: {}ml
Milk: {}ml
Coffee: {}g
Balance: ${}
"""

def print_status(water, milk, coffee, balance):
    print(PRINT_STATUS_FORMAT.format(water, milk, coffee, round(balance, 2)))

def init_quantities():
    water = WATER_Q
    milk = MILK_Q
    coffee = COFFEE_Q
    balance = 0

    return [water, milk, coffee, balance]

def add_to_balance(balance):
    penny = int(input("How many pennies? "))
    nickel = int(input("How many nickels? "))
    dime = int(input("How many dimes? "))
    quarter = int(input("How many quarters? "))

    balance += penny * CURRENCY["penny"] + nickel * CURRENCY["nickel"] + dime * CURRENCY["dime"] + quarter * CURRENCY["quarter"]
    return balance