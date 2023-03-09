from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("assets/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set Header Page
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # pdf.line(12, 22, 200, 22)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")

    for i in range(12, 273, 10):
        pdf.line(12, 12+i, 200, 12+i)

    # Set Footer
    pdf.ln(265)
    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]):
        pdf.add_page()

        for j in range(12, 273, 10):
            pdf.line(12, 12 + j, 200, 12 + j)

        # Set Footer
        pdf.ln(277)
        pdf.set_font('Arial', 'I', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
