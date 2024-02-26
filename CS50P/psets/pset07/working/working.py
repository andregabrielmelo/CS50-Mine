import re
import sys


def main():

    # Get user input (9:00 AM to 5:00 PM or 9 AM to 5 PM)
    print(convert(input("Hours: ")))


def convert(s):
    # Get two numbers written as n:nn or n, and if it's AM or PM
    time = re.search(r"\b((?:\d|1[0-2])(?::[0-6]{2})?)\b (AM|PM).[^\d-]*\b((?:\d|1[0-2])(?::[0-6]{2})?)\b (AM|PM).*", s)

    # If the did not search found it
    if not time:
        raise ValueError
    
    # Putting it all in the same format, if it received only the hours
    times = [time.group(1), time.group(3)]
    if len(times[0].split(":")) == 1:
        times[0] = f"{time.group(1)}:00"
    else:
        times[0] = time.group(1)
    if len(times[1].split(":")) == 1:
        times[1] = f"{time.group(3)}:00"
    else:
        times[1] = time.group(3)
    
    # Extracting time components (HH:MM)
    hours1, minutes1 = map(int, times[0].split(":"))
    hours2, minutes2 = map(int, times[1].split(":"))
    
    # Check if minutes is valid
    if minutes1 or minutes2 == 60:
        raise ValueError

    # Convert PM hours to 24-format 
    if time.group(2) == "PM" and hours1 != 12:
        hours1 += 12
    if time.group(4) == "PM" and hours2 != 12:
        hours2 += 12

    # Handle 12 AM case 
    if time.group(2) == "AM" and hours1 == 12:
        hours1 = 0 
    if time.group(4) == "AM" and hours2 == 12:
        hours2 = 0
    
    # Constructing the output string
    converted_time = f"{hours1:02d}:{minutes1:02d} to {hours2:02d}:{minutes2:02d}"

    return converted_time


if __name__ == "__main__":
    main()