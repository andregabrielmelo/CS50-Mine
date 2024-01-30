from string import punctuation

def main():

    # Get user input 
    while True:
        try:
            # Get user word, strip whitespaces
            user_word = input("Input: ").strip()
        except ValueError:
            pass
        else:
            break

    # Shorten word
    short_user_word = shorten(user_word)

    # Print short word
    print(f"Output: {short_user_word}")


def shorten(word):
    vogals = ["a", "e", "i", "o", "u"]
    short_word = ""
    
    for char in word:
        if char.lower() in vogals:
            char = None

        if char:
            short_word += char

    return short_word


if __name__ == "__main__":
    main()