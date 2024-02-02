import sys

def main():

    # Verify it has the correct number of command-line arguments, two [running_file, name_of_the_counted_file]
    if len(sys.argv) == 2:

        # Get the name of the file we will count
        file = sys.argv[1]

        # Try getting the extension of the file
        try:

            # Get the extension of the file
            file_extension = file.split(".")[-1]

            # See if it's a python file
            if file_extension != "py":
                raise ValueError
                
        # Exit the program if it did not receive the expected python file
        except ValueError:
                sys.exit("Not a python file")
    
    # If there is not the expected number of command-line arguments, exit
    else:
        
        # See if there is more or less command-line arguments
        if len(sys.argv) < 2:
            sys.exit("Too few command-line argumets")
        elif len (sys.argv) > 2:
            sys.exit("Too many command-line argumets")

    # Try counting the lines of the file 
    try:
        
        # Count the lines 
        lines = count_lines(file)
    
    # If the file does not exist, exit the program 
    except FileNotFoundError:
        sys.exit("File not found error")

    # Print number of lines in the file 
    print(lines)


def count_lines(file_name):

    # Counter for the number of lines
    count = 0

    # Try to open the file and count the lines
    try:
        with open(file_name, "r") as file:
            for line in file:
                if len(line.strip()) != 0 and line.lstrip()[0] != "#": # If the line is not empty and is not a comment, count it
                    count += 1

        return count
    
    # If the file is not found, raise an FileNotFoundError
    except FileNotFoundError:
       raise FileNotFoundError


if __name__ == "__main__":
    main()