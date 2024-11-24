import os
from pypdf import PdfReader

os.chdir("D:\\paras\\Assignment\\Python\\Practice\\PDF Merger\\PDFs")

reader = PdfReader("sample-1.pdf")
# print(reader)

print(f"Number of pages: {len(reader.pages)}\n\n")
print(reader.pages[0].extract_text())