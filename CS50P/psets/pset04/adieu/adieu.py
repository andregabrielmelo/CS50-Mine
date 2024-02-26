import inflect

def main():

    # Inflect engine 
    inflect_engine = inflect.engine()

    # Get user input 
    names = []
    while True:
        try:
            # Get name and put it in list
            user_names = input("Name: ").title()
            names.append(user_names)
        except EOFError: # Stop asking for input when control-d is pressed
            print()
            break

    # name, name, name, ..., name, name --> name, name, name, ..., name, and name
    names_list = inflect_engine.join(names)

    # Print adieu and names
    print(f"Adieu, adieu, to {names_list}")


main()