def main():
    # Get user input, getting rid of whitespaces 
    user_text = input("Greeting: ").strip()
    user_text_lower = user_text.lower() # put the text in lower case 

    # Print different outputs based in the input
    if user_text_lower[0:5] == "hello": # Compare the word formed by the first five letter in the string to hello
        print("$0")
    elif user_text_lower[0] == "h": # Compare the first letter of the string to h
        print("$20")
    else:
        print("$100")


main()