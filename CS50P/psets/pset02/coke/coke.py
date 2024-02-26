def main():
    buy_coke()


def buy_coke(coke_quantity=1):
    amount_due = coke_quantity * 50
    while amount_due > 0:
        # Print how much more for the coke 
        print(f"Amount Due: {amount_due}")

        # Insert coin 
        coin = int(input("Insert coin: "))

        # If the coin is valid
        if coin in [5, 10, 25]:
            # The amount diminishes depending on the coin inserted
            amount_due -= coin

    
    print(f"Change Owed: {abs(amount_due)}")

main()