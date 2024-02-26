def main():

    # User list
    user_list = {}

    # Get user input 
    while True:
        try: 
            list_item = input()
            if list_item in user_list:
                user_list[list_item] += 1
            else:
                user_list[list_item] = 1
        except EOFError:
            break
    
    # Print sorted list
    sorted_user_list = (dict(sorted(user_list.items()))) # sort list 
    for item in sorted_user_list:
        print(f"{user_list[item]} {item.upper()}")


main()