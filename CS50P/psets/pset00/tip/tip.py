def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "") # Remove $ sign
    d = float(d) # Transform d to float
    return d


def percent_to_float(p):
    p = p.replace("%", "") # Remove % sign
    p = float(p) # Transform p to float
    p = p/100 # Percentage
    return p


main()