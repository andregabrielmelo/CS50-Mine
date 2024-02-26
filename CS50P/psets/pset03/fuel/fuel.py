def main():
    # Input
    while True:
        try:
            # Get user input
            user_fraction = input("Fraction: ")
            x, y = map(int, user_fraction.split("/")) # ["n1", "n2"] --> [n1, n2]

            # Calculate percentage 
            percentage = round(100 * (x / y))

            # If it is between the expected range (0% to 100%) break out of the loop
            if 0 <= percentage <=100:
                break
        
        # Continue to ask input
        except ValueError:   
            pass
        except ZeroDivisionError:
            pass
    
    # Print the percentage based in it's value
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


main()