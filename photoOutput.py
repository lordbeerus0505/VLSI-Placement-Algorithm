from PIL import Image, ImageDraw,ImageFont
 
class photo:
    def generateImage(self):
        img = Image.new('RGB', (400, 1200), color = (73, 109, 137))
        f=open("sample.txt","r")
        heading=f.readline()
        heading=heading.split("\t")
        data=f.readlines()
        text=''
        for d in data:
            print(d+' hello')
            d=d.split("\t")
            text=text+d[0]+'                     '+d[1]
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 20)
        d.text((50,10), heading[0]+'                    '+heading[1], fill=(255,0,0))
        font = ImageFont.truetype("arial.ttf", 15)
        d.text((50,30), text, fill=(255,255,0))
        
        img.save('./static/output.png')