def main():
    height = get_height()
    print_half_pyramids(height)


def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if height in range(1, 9):
                break
            else:
                print("Invalid input. Integer between 1 and 8")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return height


def print_half_pyramids(height):
    for i in range(height):
        print(" " * (height - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))


main()
