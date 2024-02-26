import sys
from pyfiglet import Figlet, FigletFont
import random

def main():

    # Get all possible fonts 
    all_fonts = FigletFont.getFonts()

    # Verify arguments
    if len(sys.argv) == 1:

        # Get random font
        font = random.choice(all_fonts)

    elif len(sys.argv) == 3 and ("-f" == sys.argv[-2] or "--font" == sys.argv[-2]) and sys.argv[-1] in all_fonts:

        # Get the font passed by the user
        font = sys.argv[-1] # Pick last string in arguments 
    
    else:

        # Abort program
        sys.exit("Wrong commands")

    # Get user input
    while True:
        try:
            user_text = input("Input: ") 
        except ValueError:
            pass
        else:
            break 

    # Print user text
    f = Figlet(font=font)
    print(f.renderText(f"{user_text}"))

main()