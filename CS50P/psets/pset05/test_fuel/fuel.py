def main():

    # Get input
    while True:
        try:
            # Get user input
            user_fraction = input("Fraction: ")
            percentage = convert(user_fraction)

        # Ask input again if there was a error
        except (ValueError, ZeroDivisionError):
            pass

        # If not, break out of the loop
        else:
            break

    # Print the gauge based in the percentage
    print(gauge(percentage))


def convert(fraction):
    
    # Get numerator(x) and denominator(y), else it is a value error
    try:
        x, y = map(int, fraction.split("/"))  # ["n1", "n2"] --> [n1, n2]
    except ValueError:
        raise ValueError
    

    # Calculate percentage, multiplying by 100 to be between 0 and 100 instead of 0 and 1, and rouding it
    percentage = round(100 * (x / y))


    # If it is between the expected range (0% to 100%) return the percentage
    if 0 <= percentage <= 100:
        return percentage
    else:
        # Checking for type of error, ValueError or ZeroDivisionError
        if x > y:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        else:
            raise ValueError


def gauge(percentage):

    # Return the value based in the percentage
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
