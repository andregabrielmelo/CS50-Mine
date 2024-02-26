import emoji

def main():
    # Get user input 
    while True:
        try:
            user_emoji = input("Input: ")
        except ValueError:
            pass
        else:
            break   

    # Get emoji
    user_emoji = emoji.emojize(user_emoji, language="alias")

    # Print emoji
    print(f"Output: {user_emoji}")


main()