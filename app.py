from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_title(title="Topics")

df = pd.read_csv("assets/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.line(12, 20, 200, 20)

    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")

pdf.output("output.pdf")
