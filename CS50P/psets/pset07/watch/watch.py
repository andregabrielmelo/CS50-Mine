import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Get the video code after .../embed/{code}
    matches = re.search(r".*src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)\".*", s)

    # If it's found
    if matches:

        # Create a shorter version of youtube URL
        link = f"https://youtu.be/{matches.group(1)}"

        return link
    else:
        return "None"


if __name__ == "__main__":
    main()
