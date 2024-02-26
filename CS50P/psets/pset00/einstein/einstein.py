def main():
    # Get user input stripping whitespaces
    mass = int(input("m: ").strip())

    # Calculates enenrgy (E = mc^2)
    energy = mass * (300000000 ** 2)

    # Print equivalent number of joules as the mass
    print(f"E: {energy}")


main()