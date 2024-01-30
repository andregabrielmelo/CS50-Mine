from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Minimum of 2 characters and maximun of 6
    if not 2 <= len(s) <= 6:
        return False
    
    # Start with two letters
    if not s[0:2].isalpha():
        return False 

    # First number can't be 0
    for char in s:
        if char.isnumeric():
            if char == "0":
                return False
            
            break

    # Numbers can't be used in the middle
    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i + 1].isalpha():
            return False
        
    # No periods, spaces, or punctuation marks
    for char in s:
        if char in punctuation or char.isspace():
            return False
    
    return True

if __name__ == "__main__":
    main()