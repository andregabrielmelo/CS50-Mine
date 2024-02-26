def main():
    # Get user input, stripping whitespaces
    usertext = input().strip()

    # Convert emoticon to emoji
    usertext = convert(usertext)

    print(usertext)

def convert(text):
    # Replace emoticon with emoji, using the unicode code(replace + with 000)
    text = text.replace(":)", "\U0001F642")
    text = text.replace(":(", "\U0001F641")

    return text


main()