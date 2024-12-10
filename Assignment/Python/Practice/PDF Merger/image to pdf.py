from pypdf import PdfWriter, PdfReader
from PIL import Image
import os

def create_pdf_from_images(image_files, output_pdf):
    pdf_writer = PdfWriter()

    for image_file in image_files:
        if not os.path.exists(image_file):
            print(f"Error: File not found - {image_file}")
            continue  # Skip missing files

        # Open the image using PIL (Pillow)
        image = Image.open(image_file)
        
        # Convert the image to RGB (PyPDF requires this)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        
        # Save the image temporarily as a PDF
        temp_pdf = os.path.splitext(image_file)[0] + "_temp.pdf"
        image.save(temp_pdf, "PDF")
        
        # Read the temporary PDF and add its pages to the writer
        with open(temp_pdf, "rb") as temp_pdf_file:
            temp_reader = PdfReader(temp_pdf_file)
            for page in temp_reader.pages:
                pdf_writer.add_page(page)

        # Clean up the temporary file
        os.remove(temp_pdf)
    
    # Write the combined PDF to the output file
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"PDF created successfully at {output_pdf}")

# Example usage
images = [
    r"D:\paras\\Assignment\Python\Practice\PDF Merger\1.jpg",
    r"D:\paras\\Assignment\Python\Practice\PDF Merger\2.jpg",
    r"D:\paras\\Assignment\Python\Practice\PDF Merger\3.jpg",
    r"D:\paras\\Assignment\Python\Practice\PDF Merger\4.jpg"
]
output = r"D:\paras\Assignment\Python\Practice\PDF Merger\paras.pdf"
create_pdf_from_images(images, output)
