import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    # Get all matches of um in the string
    all_matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    # Return the lenght of a list with all times um appeared in the string ("um", "um", "um",...)
    return len(all_matches)


if __name__ == "__main__":
    main()