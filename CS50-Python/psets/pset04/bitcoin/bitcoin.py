import sys
import requests

def main():

    # Verift if it has 2 command line arguments
    if not len(sys.argv) == 2:
        sys.exit("Missing command-line argument")
    
    # Verify it's a valid argument 
    try:
        quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get CoinDesk Bitcoin Price Index 
    try:
        # Querie the API
        request_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # If the return is not positive, not 200, exit 
        if request_price.status_code != 200:
            raise requests.RequestException
        
    except requests.RequestException:
        sys.exit("Error during request") # needed?
    
    # Get the bitcoin price in float inside the json in the request_price
    bitcoin_price = request_price.json()["bpi"]["USD"]["rate_float"]

    # Print the price of bitcoin times the quantity inserted by the user, using ',' as a thounsand separator and 4 decimal places
    print(f"${(quantity * bitcoin_price):,.4f}")


main()