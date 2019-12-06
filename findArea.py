import numpy as np
import cv2

def calcArea(path):
    image=cv2.imread(path,0)
    ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
    # print(thresh1)
    # cv2.imwrite("thresh.png",thresh1)
    #presuming its always a rectangle
    left=1000
    right=0
    top=1000
    bot,flag1,flag2=0,0,0
    dim=thresh1.shape
    # import pdb; pdb.set_trace()
    for i in range(dim[0]-10): #last few lines used in one black line drawn
        for j in range(dim[1]):
            if thresh1[i][j]==0 and flag1==0:
                top=i
                flag1=1
            if thresh1[i][j]==0 and left>j:
                left=j
                break
            if thresh1[i][j]==0 and bot<i:
                bot=i
        for j in range(dim[1]-1,0,-1):
            if thresh1[i][j]==0 and right<j:
                right=j
                break

    print(left,"is the left most black")
    print(right,"is the right most black")
    print(top,"is the top most black")
    print(bot,"is the bot most black")

    Length=bot-top
    Width=right-left

    Area=Length*Width
    return Area,Length,Width #if any aspect needed, can adjust using dimensions

print(calcArea("icDiagram.jpeg")) #find out units