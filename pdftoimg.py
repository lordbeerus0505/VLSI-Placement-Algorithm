from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
def pdftoimage(path):
    images = convert_from_path(path)
    # print(path[:-3]+"pdf")
    # images[0].save(path[:-3]+"png")
    images[0].save("pdfimg.png")

pdftoimage("report.pdf")