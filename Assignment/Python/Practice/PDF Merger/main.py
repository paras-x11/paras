# PdfReader example: Reading and extracting text from a PDF
from pypdf import PdfReader

# Method: PdfReader("filename") - Opens a PDF file.
reader = PdfReader("example.pdf")

# Method: .pages - List of all pages in the PDF.
first_page = reader.pages[0]

# Method: .extract_text() - Extracts text content from a page.
text = first_page.extract_text()
print(f"Text from the first page:\n{text}")

# PdfWriter example: Creating and modifying a PDF
from pypdf import PdfWriter, PdfReader

reader = PdfReader("example.pdf")
writer = PdfWriter()

# Method: .add_page(page) - Adds a page to the writer.
writer.add_page(reader.pages[0])

# Method: .add_metadata(metadata) - Adds metadata to the PDF (e.g., author, title).
writer.add_metadata({
    "/Author": "John Doe",
    "/Title": "Example PDF"
})

# Method: .encrypt(password) - Encrypts the PDF with a password.
writer.encrypt("password123")

# Method: .write(file) - Writes the modified PDF to a file.
with open("output.pdf", "wb") as output_file:
    writer.write(output_file)
print("PDF created successfully!")

# PdfMerger example: Merging multiple PDFs into one
from pypdf import PdfMerger

merger = PdfMerger()

# Method: .append(file) - Appends a PDF file to the merger.
merger.append("file1.pdf")
merger.append("file2.pdf")

# Method: .merge(position, file) - Merges pages from another PDF at a specific position.
merger.merge(1, "file3.pdf")

# Method: .write(file) - Writes the merged PDF to a new file.
with open("merged_output.pdf", "wb") as output_file:
    merger.write(output_file)

# Method: .close() - Finalizes the merging process.
merger.close()
print("PDFs merged successfully!")

