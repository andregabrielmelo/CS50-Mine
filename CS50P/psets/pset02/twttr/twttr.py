def main():
    user_text = input("Input: ")
    output = ""

    for char in user_text:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            char = None
    
        if char:
            output += char

    print(f"Outuput: {output}")

main()