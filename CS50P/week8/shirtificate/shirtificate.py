from fpdf import FPDF


def main():
    user_input = input("Name: ")
    return user_input

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 5, 60, 200,)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title & other text:
        self.cell(30, 10, "CS50 Shirtificate", align="C")

user_input = main()


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", "B", size=20)
pdf.set_text_color(255, 255, 255)
pdf.cell(-30, 220, f"{user_input} took CS50", align="C")
pdf.output("shirtificate.pdf")
