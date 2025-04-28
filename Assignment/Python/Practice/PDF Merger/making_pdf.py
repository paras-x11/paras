# Fix: Replace '→' with '=>'
# Re-create the PDF properly without special symbols

from fpdf import FPDF

class PDFFixed(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Python - Type Conversion, Precedence, and Associativity', ln=True, align='C')
        self.ln(10)

    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def add_table(self, col_widths, headings, data):
        self.set_font('Arial', 'B', 12)
        for i, heading in enumerate(headings):
            self.cell(col_widths[i], 10, heading, border=1, align='C')
        self.ln()
        self.set_font('Arial', '', 12)
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), border=1, align='C')
            self.ln()
        self.ln(5)

pdf = PDFFixed()
pdf.add_page()

# Section 1 - Type Conversion
pdf.section_title("1. Type Conversion in Python")

headings = ["Type", "Meaning", "Example", "Notes"]
data = [
    ["Implicit Conversion", "Auto smaller to larger type", "int + float => float", "No manual action"],
    ["Explicit Conversion", "Manually change type", "int('5') => 5", "Use int(), float(), str()"]
]
col_widths = [40, 60, 45, 45]
pdf.add_table(col_widths, headings, data)

# Functions Table
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "Functions for Explicit Conversion:", ln=True)
headings = ["Function", "Purpose", "Example"]
data = [
    ["int(x)", "Convert to integer", "int('123') => 123"],
    ["float(x)", "Convert to float", "float('12.3') => 12.3"],
    ["str(x)", "Convert to string", "str(123) => '123'"],
    ["list(x)", "Convert to list", "list('abc') => ['a','b','c']"],
    ["tuple(x)", "Convert to tuple", "tuple([1,2,3]) => (1,2,3)"],
    ["set(x)", "Convert to set", "set([1,2,2,3]) => {1,2,3}"]
]
col_widths = [40, 65, 65]
pdf.add_table(col_widths, headings, data)

# Section 2 - Operator Precedence
pdf.section_title("2. Operator Precedence in Python")
headings = ["Precedence", "Operators", "Description"]
data = [
    ["1", "()", "Parentheses"],
    ["2", "**", "Exponent"],
    ["3", "+x, -x, ~x", "Unary operations"],
    ["4", "*, /, //, %", "Multiplication, Division, Modulus"],
    ["5", "+, -", "Addition, Subtraction"],
    ["6", "<<, >>", "Bitwise Shift"],
    ["7", "&", "Bitwise AND"],
    ["8", "^", "Bitwise XOR"],
    ["9", "|", "Bitwise OR"],
    ["10", "in, is, ==, !=", "Comparison, Membership, Identity"],
    ["11", "not", "Logical NOT"],
    ["12", "and", "Logical AND"],
    ["13", "or", "Logical OR"],
    ["14", "=", "Assignment"]
]
col_widths = [25, 55, 110]
pdf.add_table(col_widths, headings, data)

# Section 3 - Associativity
pdf.section_title("3. Associativity of Operators in Python")
headings = ["Operator Group", "Examples", "Associativity Direction"]
data = [
    ["Exponent", "**", "Right to Left"],
    ["Arithmetic", "+, -, *, /, %, //", "Left to Right"],
    ["Bitwise Operators", "&, |, ^, <<, >>", "Left to Right"],
    ["Comparison Operators", "<, >, ==, !=", "Left to Right"],
    ["Logical Operators", "not, and, or", "Left to Right"],
    ["Assignment Operators", "=, +=, -=", "Right to Left"]
]
col_widths = [50, 60, 80]
pdf.add_table(col_widths, headings, data)

# Section 4 - Examples
pdf.section_title("4. Examples")
headings = ["Example", "Output", "Explanation"]
data = [
    ["2 + 3 * 4", "14", "Multiplication first"],
    ["(2 + 3) * 4", "20", "Parentheses change order"],
    ["2 ** 3 ** 2", "512", "Right to Left for **"],
    ["5 - 2 - 1", "2", "Left to Right for -"],
    ["a = b = c = 10", "10", "Assignment is Right to Left"]
]
col_widths = [50, 30, 110]
pdf.add_table(col_widths, headings, data)

# Section 5 - Final Summary
pdf.section_title("5. Final Quick Summary")
headings = ["Topic", "Python Behavior"]
data = [
    ["Type Conversion", "Both Implicit and Explicit"],
    ["Operator Precedence", "Fixed priority order"],
    ["Operator Associativity", "Mostly Left-to-Right, some Right-to-Left"]
]
col_widths = [70, 120]
pdf.add_table(col_widths, headings, data)

# Save the new fixed pdf
final_fixed_pdf_path = "Python_TypeConversion_Precedence_Associativity_NiceTable.pdf"
pdf.output(final_fixed_pdf_path)

final_fixed_pdf_path
