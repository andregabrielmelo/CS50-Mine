from tabulate import tabulate
import csv
import sys

def main():

    # Verify if it has the expected command-line arguments
    if len(sys.argv) != 2:

        # See if there is more or less arguments
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")

    # Get file name
    file_name = sys.argv[1]

    # Get file extension 
    file_extension = file_name.split(".")[-1] 

    # Verify it's a CSV file 
    if file_extension != "csv":
        sys.exit("Not a CSV file")

    # Read the CSV file
    try:
        with open(file_name, "r") as file:

            # Create a dict reader obj
            reader = csv.DictReader(file)

            # Make a table with each row of the CSV file
            table = [row for row in reader]

    # If the file is not found, exit
    except FileNotFoundError:
        sys.exit("Could not find file")

    # Output table formatted as ASCII art, the table content is in table, and the headers will be the keys in the table
    print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()