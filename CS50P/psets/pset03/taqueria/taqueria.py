def main():
    # Menu
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Get order
    total = 0
    while True:
        try:
            # Item on the menu the user wants
            user_item = input("Item: ")
            user_item = user_item.title()
            
            # If it is really in the menu, add to the total the user has to pay
            if user_item in menu:
                total += menu[user_item]
                print(f"Total: ${total:.2f}")
        
        # Control-d exit the program
        except EOFError:
            print() # New line
            break


main()