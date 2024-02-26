def main():

    # List of the months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Get date in anno Domini format (month-day-year, Month day, year or month/day/year) 
    while True:
        try:
            # Input date 
            user_date = input("Date: ")

            # Get month, day and year
            if "," in user_date:
                user_date = user_date.replace(",","")
                month = months.index(user_date.split(" ")[0]) + 1
                day, year = map(int, user_date.split(" ")[1:])
            elif "-" in user_date:
                month, day, year = map(int, user_date.split("-"))
            elif "/" in user_date:
                month, day, year = map(int, user_date.split("/"))
            else:
                raise ValueError # There is a error in how the user put the date 

            # Verify if it it's acceptable
            if not (1 <= day <= 31 and 1 <= month <= 12):
                raise ValueError() # Date or month is out of bounds
        except ValueError:
            pass
        else:
            break

    print(f"{year}-{month:02}-{day:02}")

main()