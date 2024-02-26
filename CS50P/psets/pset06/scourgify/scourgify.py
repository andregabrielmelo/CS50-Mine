import sys
import csv


def main():

    # Verify it has the expected amount of command-line arguments (python3 scourgify.py before.csv after.csv)
    if len(sys.argv) != 3:

        # See if it has more or less arguments than expected, and exit
        if len(sys.argv) > 3:
            sys.exit("Too many arguments")
        else:
            sys.exit("Too few arguments")

    # Get files names
    file_before = sys.argv[1]
    file_after = sys.argv[2]

    # Get files extensions
    file_extensions = [file_before.split(".")[-1], file_after.split(".")[-1]]

    # Verify both are a CSV file
    if file_extensions != ["csv", "csv"]:
        sys.exit("Both need to be a CSV file")

    # Read the CSV file_before
    try:
        with open(file_before, "r") as file_1, open(file_after, "w") as file_2:

            # Create a dict objects
            reader = csv.DictReader(file_1)
            writer = csv.DictWriter(file_2, fieldnames=["first", "last", "house"])

            # Write header in the file_2 (after)
            writer.writeheader()

            # Read the file_1 (before) and write it in file_2 (after), separating name in first and last, (name, house) --> (first, last, house)
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

    # If the file to read (before) is not found, exit
    except FileNotFoundError:
        sys.exit(f"Could not find {file_before}")


if __name__ == "__main__":
    main()
