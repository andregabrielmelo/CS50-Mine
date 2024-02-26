def main():
    # Get user input, stripping whitespaces and the splitting it
    usertext = input("").strip().split()
    
    # Join the words in usertext, using ... when there would be normally a space
    usertext = "...".join(usertext)

    print(usertext)


main()