import pandas as pd
from fpdf import FPDF
import time
import sys

print(sys.path)
print(sys.version)

def create_pdf():
  WIDTH = 215.9
  HEIGHT = 279.4
  pdf = FPDF() # 8.5 x 11 (215.9 by 279.4 mm)
  # compression is not yet supported in py3k version
  pdf.compress = False
  pdf.add_page()
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', '', 14)  
  pdf.ln(10)
  pdf.write(5, f"Covid Analytics Report")
  pdf.ln(5)
  pdf.set_font('Arial', '', 10)
  pdf.write(4, '10/24/2020')
  pdf.image("Massachusetts_7.png", 5, 30, WIDTH/2-10)
  pdf.image("New Hampshire_7.png", WIDTH/2, 30, WIDTH/2-10)
  pdf.image("Massachusetts_30.png", 5, 100, WIDTH/2-10)
  pdf.image("New Hampshire_30.png", WIDTH/2, 100, WIDTH/2-10)
  pdf.output('py3k.pdf', 'F')

create_pdf()