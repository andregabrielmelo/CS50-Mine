import sys
from PIL import Image, ImageOps

def main():

    # Verify it has the expected amount of command-line arguments (python3 scourgify.py before.csv after.csv)
    if len(sys.argv) != 3:

        # See if it has more or less arguments than expected, and exit
        if len(sys.argv) > 3:
            sys.exit("Too many arguments")
        else:
            sys.exit("Too few arguments")

    # Get files names
    file_before = sys.argv[1]
    file_after = sys.argv[2]

    # Get files extensions
    file_extensions = [file_before.split(".")[-1],file_after.split(".")[-1]]

    # Verify both files are a JPG, JPEG or PNG file
    if all(extension not in ["jpg", "jpeg", "png"] for extension in file_extensions):
        sys.exit("Both need to be a JPG, JPEG or PNG file")

    # Verify if input and output file have the same extension
    if file_extensions[0] != file_extensions[1]:
        sys.exit("Input and output have different extensions")

    # Modify images
    with Image.open(file_before, mode="r") as image, Image.open("shirt.png") as shirt:

        # Get the dimensions of the shirt image 
        width, height = shirt.size  

        # Change image size
        image = ImageOps.fit(image, (width, height))

        # Paste shirt in image 
        image.paste(shirt, (0, 0), shirt)

        # Save image
        image.save(file_after)


if __name__ == "__main__":
    main()