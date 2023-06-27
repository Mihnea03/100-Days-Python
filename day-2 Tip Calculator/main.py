# Tip Calculator
# Munteanu Mihnea @ Mihnea03

def main():
    print("Welcome to the tip calculator.")

    total_bill = float(input("What was the total bill? $"))
    people = int(input("How many people to split the bill? "))
    tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

    total_pay = total_bill + (float(tip) / 100) * total_bill

    each_person_pay = round(float(total_pay / people), 2)
    print("Each person should pay: ${}".format(each_person_pay))

if __name__ == '__main__':
    main()