def main():
    # Get user input and strip whitespaces
    user_input = input("What time is it? ").strip()
    
    # Convert user input to a time
    time = convert(user_input)  

    # Print something if it's meal time 
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    # Get hour and minutes  
    hour, minutes = time.split(":")

    # Convert to float
    hour = float(hour)

    # Change the time if it have a.m. or p.m.
    if "a.m." in minutes:
        minutes = minutes.replace("a.m.", "")
    elif "p.m." in minutes:
        minutes = minutes.replace("p.m.", "")
        hour += 12

    return (hour + float(minutes)/60)



if __name__ == "__main__":
    main()