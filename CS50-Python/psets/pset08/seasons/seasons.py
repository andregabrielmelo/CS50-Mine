from datetime import date, datetime
import inflect
import sys


def main():
    inflect_engine = inflect.engine()

    # Get date of birth (YYYY-MM-DD)
    user_date_of_birth = input("Date of Birth: ")

    # Try to calculate how old a pearson is
    try:
        user_minutes_of_life = how_old(user_date_of_birth)
    except ValueError:
        sys.exit("Invalid data format")

    answer = inflect_engine.number_to_words(user_minutes_of_life, andword="")

    print(f"{answer.capitalize()} minutes") 


def how_old(birth_date):
    # Born at midnight and the current time is also midnight (00:00:00) 

    # Transform birth date into a data object
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid data format")

    # Calculate the number of days bwtween those two dates
    days_difference = (date.today() - birth_date).days

    # Calculate in minutes 
    min_difference = days_difference * 24 * 60

    return min_difference


if __name__ == "__main__":
    main()