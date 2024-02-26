from fpdf import FPDF
from PIL import Image
import sys

def main(): # TODO:Calculate the values

    # Get name 
    name = input("Name: ").strip()
    if not name:
        sys.exit("No name")

    # Create pdf, A4 210mm X 297mm
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "I", 8)

    # I took CS50
    pdf.set_font_size(40)
    pdf.set_y(20)  # Set y position
    pdf.cell(0, 10, f"CS50 Shirtificate", align="C")  # Center align the text                        

    # Open the image file
    image = Image.open("shirtificate.png")

    # Get image dimensions
    image_width, image_height = image.size

    # Calculate scaling factor to fit the image within the page width
    page_width = pdf.w
    page_height = pdf.h
    scale_factor = page_width / image_width

    # Calculate scaled image dimensions
    new_width = (image_width * scale_factor) / 1.25
    new_height = (image_height * scale_factor) / 1.25

    # Calculate center position for the image horizontally
    x_position = (page_width - new_width) / 2
    y_position = (page_height - new_height) / 2

    # Add the image
    pdf.image("shirtificate.png", x=x_position, y=y_position, w=new_width)

    # Calculate the height of the text based on the position of the image
    text_height = y_position + (new_height * 5/20)  # Adjust this value as needed

    # Add the text below the image
    pdf.set_y(text_height)  # Set y position
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(20)
    pdf.cell(0, 10, f"{name.capitalize()} took CS50", align="C")  # Center align the text                        

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
