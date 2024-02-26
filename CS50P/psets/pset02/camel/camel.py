def main():
    # Get user input and strip whitespaces
    user_text = input("camelCase: ").strip()

    # Print the user input in snake case
    print(convert_camel_to_snake(user_text))


def convert_camel_to_snake(text):
    converted_text = ""
    for char in text:
        if char.isupper():
            converted_text += f"_{char.lower()}"
        else:
            converted_text += char

    return converted_text

main()