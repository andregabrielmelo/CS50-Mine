import sys


def main():
    # Ensure correct usage
    if len(sys.argv) != 1:
        sys.exit("Usage: python hello.py")

    name = get_name()
    print(f"hello, {name}")


def get_name():
    print("What is your name?")
    name = str(input())  # Gets user input

    return name


main()
