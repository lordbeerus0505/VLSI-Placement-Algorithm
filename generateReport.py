from fpdf import FPDF
from PIL import Image
import PIL
import cv2
import imutils
pdf = FPDF()
# imagelist is the list with all image filenames
imagelist=['arch.jpg','blockchain.jpg','book.png','database.png','pdfimg.png' ,'output.png','icDiagram.jpg']
def generatePDF(imagelist,outputlist):
    width,height=600,900
    for i in range(len(imagelist)):
        img=Image.open(imagelist[i])
        if img.size[1]<img.size[0] :
            baseWidth=500
            wpercent=(baseWidth/float(img.size[0]))
            hsize=int((float(img.size[1]) * float(wpercent)))
            img = img.resize((baseWidth, hsize), PIL.Image.ANTIALIAS)
            img.save("output_"+str(imagelist[i][:-3])+'png')
        else:
            baseheight = 800
            hpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            if wsize<600:
                img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
            else:
                img = img.resize((550,550), PIL.Image.ANTIALIAS)
            img.save("output_"+str(imagelist[i][:-3])+'png')
        # pdf.add_page()
        # pdf.image("output_"+str(imagelist[i][:-3])+'.png',20,20)
    # for i in range(len(imagelist)):
    #     cover = Image.open(str(imagelist[i]) )
    #     if cover.size[0]>width:
    #         width=cover.size[0]
    #     if cover.size[1]>height:
    #         height=cover.size[1]
    # 
    pdf = FPDF(unit = "pt", format = [width, height])
    for image in outputlist:
        pdf.add_page()
        img=Image.open(image)
        print(img.size)
        width=img.size[0]
        height=img.size[1]
        left=(600-width)/2
        top=(900-height)/2
        pdf.image(image,left,top)
    pdf.output("report.pdf", "F")

outputlist=['output_arch.png','output_blockchain.png','output_book.png','output_database.png','output_pdfimg.png' ,'output_output.png','output_icDiagram.png']
generatePDF(imagelist,outputlist)