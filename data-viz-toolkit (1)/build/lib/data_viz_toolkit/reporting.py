from fpdf import FPDF

def generate_report(charts, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="DataViz Report", ln=True, align='C')

    for chart in charts:
        pdf.cell(200, 10, txt=chart, ln=True)

    pdf.output(filename)
