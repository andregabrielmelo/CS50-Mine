import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # Get all of the four numbers on the IP adress
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)

    # If the search happened without errors and all numbers are within boundaries
    if matches and all(0 <= int(number) <= 255 for number in matches.groups()):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
