from fpdf import FPDF

class HindiPDF(FPDF):
    pass

def generate_report(name, schemes):

    pdf = HindiPDF()
    pdf.add_page()

    pdf.add_font("Noto","",
                 "NotoSansDevanagari-Regular.ttf",uni=True)
    pdf.set_font("Noto",size=14)

    pdf.cell(0,10,"सरकारी योजना पात्रता रिपोर्ट",new_x="LMARGIN",new_y="NEXT")
    pdf.cell(0,10,f"नाम: {name}",new_x="LMARGIN",new_y="NEXT")
    pdf.ln(8)

    for s in schemes:

        pdf.set_font("Noto",size=13)
        pdf.cell(0,10,s["name"],new_x="LMARGIN",new_y="NEXT")

        pdf.set_font("Noto",size=12)
        pdf.multi_cell(0,8,s["benefit"])

        pdf.set_text_color(0,0,255)
        pdf.cell(0,8,"आवेदन लिंक",
                 link=s["apply_link"],
                 new_x="LMARGIN",new_y="NEXT")
        pdf.set_text_color(0,0,0)

        pdf.ln(5)

    return bytes(pdf.output(dest="S"))