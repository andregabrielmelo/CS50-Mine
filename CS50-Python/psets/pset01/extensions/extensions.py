def main():
    # Get user input and strip whitespaces
    user_file = input("File name: ").strip()

    # Get file extension
    extension = user_file.split(".")[-1].lower() # Split string with period as sep, get last element of the lsit, and put it in lower case

    # Print media type based on the file extension (text after the period)
    if extension in ["gif", "jpg", "jpeg", "png"]:
        if extension == "jpg": # jpg is image/jpeg media type
            extension = "jpeg"
        
        print(f"image/{extension}")
    elif extension in ["pdf", "zip"]:
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")


main()