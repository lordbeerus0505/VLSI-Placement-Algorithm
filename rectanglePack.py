import  rpack
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import cv2

def calcArea(a,b,c):
    l1=c-a[1]
    b1=b-a[0]
    # import pdb; pdb.set_trace()
    return l1*b1

# 5915
# 3760
# 5500
# 7910
# 1200
# 30000
# 54285 Total area

sizes=[
    (65,	91),(47	,80),(50	,110),(70,	113),(40,	30),(200,	150),
]
# sizes = [
# (200,	150),
# (70,	113),
# (50	,110),
# (65,	91),
# (47	,80),
# (40,	30),
# ]
positions = rpack.pack(sizes)
print(positions)
fig,ax = plt.subplots(1)
im = np.zeros([500,500,3],dtype=np.uint8)
im.fill(255) # or img[:] = 255
# Display the image
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(im)

# import pdb; pdb.set_trace()
# Create a Rectangle patch
rect=[]
area=10000
count=0
for p in positions:
    rect.append(patches.Rectangle(p,sizes[count][0],sizes[count][1],linewidth=1,edgecolor='r',facecolor='none'))
    if abs(calcArea(p,sizes[count][0],sizes[count][1]))<area:
        area=abs(calcArea(p,sizes[count][0],sizes[count][1]))
        # import pdb; pdb.set_trace()
    count+=1

# import pdb; pdb.set_trace()
#finding scaling factor
sf=area/1200
# Add the patch to the Axes
for i in range(6):
    ax.add_patch(rect[i])

# ax.add_patch(patches.Rectangle((top_left),max(x)-min(x),max(y)-min(y),linewidth=2,edgecolor='b',facecolor=None))
# plt.show()
# plt.savefig('result.png', bbox_inches='tight')
fig.savefig('out_tier12.png', bbox_inches='tight', pad_inches=0)

image=cv2.imread('out_tier12.png',0)

ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
left=1000
right=0
top=1000
bot,flag1,flag2=0,0,0
dim=thresh1.shape
# import pdb; pdb .set_trace()

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
color = (0, 0, 255) 
Length=bot-top
Width=right-left
image = cv2.rectangle(image, (0,0), (Width,Length), color, 2) 
Area=Length*Width
# import pdb; pdb.set_trace()
print(Area/570*1200)
cv2.imshow("Image",image)
cv2.waitKey()