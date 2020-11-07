from fpdf import FPDF
import os

pdf_w = 210
pdf_h = 297
card_w = 63.5
card_h = 88.9
num_width = 3
num_height = 3

margin_top = (pdf_h-num_height*card_h)/2
margin_left = (pdf_w-num_width*card_w)/2

class PDF(FPDF):
    pass

pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

i = 0
for filename in os.listdir("../images"):
    if i >= num_width*num_height:
        pdf.add_page()
        i = 0
    x = i % num_width
    y = i // num_width
    i += 1
    x_offset = margin_left+x*card_w
    y_offset = margin_top+y*card_h
    pdf.image("../images/"+filename, x_offset, y_offset, card_w, card_h)
    # pdf.rect(x_offset, y_offset, card_w, card_h, style='F')
#
pdf.output('../output/output.pdf', 'F')
