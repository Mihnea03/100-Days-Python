# Calculator
# Munteanu Mihnea @ Mihnea03

def calculate(first_number, operator, second_number):
    result = 0

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number

    return round(result, 3)

def main():

    quit = False
    first_calculated = False
    result = 0

    while quit is False:

        if first_calculated is False:
            first_number = float(input("What's the first number? "))
        else:
            first_number = result

        operator = str(input("Type '+', '-', '*' or '/': "))

        second_number = float(input("What's the second number? "))

        result = calculate(first_number, operator, second_number)
        print(f"The result is: {result}\n")

        q = str(input("Type 'q' to quit, 'n' to use the result as the first number or 'y' to try another operation\n"))

        if q == 'q':
            quit = True
        elif q == 'n':
            first_calculated = True
            continue
        elif q == 'y':
            first_calculated = False
            continue
    return

if __name__ == '__main__':
    main()
