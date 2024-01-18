import math


def main():
    card_number = input("Number: ")  # Read the card number as a string
    card_type(card_number)  # Print wich company the card is from


def luhn_algorithm(card_number):  # Sum of the numbers in the card using luhn_algorithm
    sum = 0
    for i in range(len(card_number)):
        digit = int(card_number[len(card_number) - 1 - i])  # Begins at the last digit
        if i % 2 == 0:
            sum += digit
        else:
            digit *= 2
            sum += digit // 10 + digit % 10
    return sum


def card_type(card_number):
    size = len(card_number)  # The number of digits the card has
    sum = luhn_algorithm(card_number)

    # Important information on the card
    # print(f"Size: {size}")
    # print(f"Sum: {sum}")
    # print("Digits: " + card_number[0:2])

    if sum % 10 == 0:
        if card_number[0:2] in ["34", "37"] and size == 15:
            print("AMEX")
        elif card_number[0:2] in ["51", "55"] and size == 16:
            print("MASTERCARD")
        elif card_number[0] == "4" and 13 <= size <= 16:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
