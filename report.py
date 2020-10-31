# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta

# Local libraries
from time_series_analysis import plot_states, plot_countries
from create_case_maps import plot_usa_case_map, plot_global_case_map

yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y")
# Uncomment below line for testing
#yesterday = "10/10/20"

WIDTH = 215.9
HEIGHT = 279.4

def create_title(pdf):
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', '', 24)  
  pdf.ln(60)
  pdf.write(5, f"Covid Analytics Report")
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{yesterday}')
  pdf.ln(5)

def create_pdf_local(filename="local.pdf"):
  pdf = FPDF() # 8.5 x 11 (215.9 by 279.4 mm)
  pdf.add_page()
  create_title(pdf)

  plot_states(['Massachusetts', 'New Hampshire'], filename="tmp/cases.png")
  plot_states(['Massachusetts', 'New Hampshire'], mode="Deaths", filename="tmp/deaths.png")
  plot_usa_case_map("test2.png")
  plot_global_case_map("test3.png")


  pdf.image("tmp/cases.png", 5, 40, WIDTH/2-10)
  pdf.image("tmp/deaths.png", WIDTH/2, 40, WIDTH/2-10)
  pdf.image("test2.png", 5, 120, WIDTH/2-10)
  pdf.image("test3.png", WIDTH/2, 120, WIDTH/2-10)
  pdf.output(filename, 'F')

def create_pdf_global(filename="global.pdf"):
  pdf = FPDF() # 8.5 x 11 (215.9 by 279.4 mm)
  pdf.add_page()
  create_title(pdf)

  plot_usa_case_map("test2.png")
  plot_global_case_map("test3.png")

  offset = 5
  pdf.image("test2.png", offset, 40, WIDTH-4*offset)
  pdf.image("test3.png", offset, 150, WIDTH-4*offset)
  pdf.output('py3k.pdf', 'F')

def create_pdf_usa(filename="usa.pdf"):
  pdf = FPDF() # 8.5 x 11 (215.9 by 279.4 mm)
  pdf.add_page()
  pdf.image("background_cropped.jpeg", -13, 0, h=HEIGHT+17.5)
  create_title(pdf)


  plot_usa_case_map("test2.png")
  plot_states(['Massachusetts', 'New Hampshire'], filename="tmp/cases.png")
  plot_states(['Massachusetts', 'New Hampshire'], mode="Deaths", filename="tmp/deaths.png")


  offset = 5
  pdf.image("test2.png", offset, 80, WIDTH-4*offset)
  pdf.image("tmp/cases.png", 5, 190, WIDTH/2-10)
  pdf.image("tmp/deaths.png", WIDTH/2, 190, WIDTH/2-10)

  pdf.output(filename, 'F')

def create_pdf_usa2(filename="usa.pdf"):
  pdf = FPDF() # 8.5 x 11 (215.9 by 279.4 mm)
  pdf.add_page()
  pdf.image("background2.png", -3, 0, WIDTH)
  create_title(pdf)


  plot_usa_case_map("test2.png")
  plot_states(['Massachusetts', 'New Hampshire'], days=250, filename="tmp/cases2.png")
  plot_states(['Massachusetts', 'New Hampshire'], days=250, mode="Deaths", filename="tmp/deaths.png")

  offset = 5
  pdf.image("test2.png", offset, 90, WIDTH-4*offset)
  pdf.image("tmp/cases2.png", 5, 200, WIDTH/2-10)
  pdf.image("tmp/deaths.png", WIDTH/2, 200, WIDTH/2-10)

  pdf.add_page()
  pdf.image("test2.png", offset, 90, WIDTH-4*offset)
  pdf.image("tmp/cases.png", 5, 200, WIDTH/2-10)
  pdf.image("tmp/deaths.png", WIDTH/2, 200, WIDTH/2-10)

  pdf.output(filename, 'F')

create_pdf_usa2()