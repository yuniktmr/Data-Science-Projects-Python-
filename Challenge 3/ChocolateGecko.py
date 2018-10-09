#ChocolateGecko
#Challenge 3
#Last edited: March 9
#Source: Lecture, StackOverflow
import matplotlib.pyplot as mplot
from PIL import Image
import glob
import numpy as np
#list of images
imgsList = (glob.glob(r'C:\Users\yunik\Documents\CSCI 343\Challenge 3\unionconstruction\*.jpg'))
imgList=[]
first = True
sumImage=0
threshold=int(input("Enter the threshold value"))
for i in imgsList:
    image=Image.open(i)
    imgList.append(np.float32(image))
    temp = np.asarray(image)
    temp = temp.astype('float32')
    if first:
        sumImage = temp
        first = False
    else:
        sumImage = sumImage + temp
#averaging
avgArray = sumImage/len(imgsList)
avgArray=np.clip(avgArray, 0, 255)
s=0
for i in imgList:
    s=s+(i - avgArray)**2
sd=np.sqrt(s/len(imgList))
sd=np.clip(sd, 0, 255)
#highlighting in red
for row in range(0,len(avgArray)):
    for col in range(0,len(avgArray[row])):
        if(sd[row][col]>threshold).any():
            avgArray[row][col]=(255,0,0)
sdImg=Image.fromarray(sd.astype('uint8'))
avgImg = Image.fromarray(avgArray.astype('uint8'))
print(avgImg)
mplot.imshow(avgImg)
mplot.show()
# mplot.imshow(sdImg)
# mplot.show()
