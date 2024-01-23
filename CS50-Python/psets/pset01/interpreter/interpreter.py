def main():
    # Get user input and get rid of whitespaces
    user_input = input("Expression: ").strip() # x operator y

    # Get two operands and an operator
    x, operator, y = user_input.split(" ")
    
    # Output a operation with the two operands (x, y) based in the operator
    print(operation(operator, float(x), float(y)))

def operation(operator, x, y):
    if operator == "+":
        return (x + y)
    elif operator == "-":
        return (x - y)
    elif operator == "*":
        return (x * y)
    elif operator == "/":
        return (x / y)


main()