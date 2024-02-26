def main():
    # Get user input as str and clean whitespaces, turn into lower case 
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    if user_input in ["42", "forty two", "forty-two"]:
        print("Yes")
    else:
        print("No")


main()