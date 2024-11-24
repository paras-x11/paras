from pypdf import PdfWriter
import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\PDF Merger\\PDFs")

merger = PdfWriter()

merger.append("sample-1.pdf")
merger.append("sample-2.pdf")

merger.merge(1, "sample-3.pdf")

with open("merged_output.pdf", 'wb') as merged_output:
    merger.write(merged_output)

