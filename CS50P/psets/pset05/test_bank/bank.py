def main():

    # Get user input, getting rid of whitespaces 
    while True:
        try:
            user_text = input("Greeting: ").strip() 
        except ValueError:
            pass
        else: 
            break

    # Print different outputs based in the input
    quantity = value(user_text)
    print(f"${quantity}")
    

def value(greeting):

    # Pass to lowercase
    greeting = greeting.lower() 
    
    # Different quantites of money
    if greeting[0:5] == "hello": # Compare the word formed by the first five letter in the string to hello
        return 0
    elif greeting[0] == "h": # Compare the first letter of the string to h
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()



    
    
    
 