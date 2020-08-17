import cv2
import numpy as np


#Pick an image to analyze
img = cv2.imread('cube.jpg')

#Coordinates we need to extract [y,x], y increasing downwards
coordinates = 84,141

#color outputs as [B G R]
pxl = img[coordinates]



#Print pxl, RGB values
print(pxl)



#returns a List of coordinates, read from a txt file
def getCoordinatesArray(filename):
    file = open(filename, "r")
    upList, rightList, fwdList,downList, leftList, backList = [],[],[],[],[],[]

    list = []
    for line in file:
        list.append(line.strip().split('\n'))

    
    for x in range(0,6):
        upList.append(tuple(list[x]))
    for x in range(6,12):
        rightList.append(tuple(list[x]))
    for x in range(12,18):
        fwdList.append(tuple(list[x]))
    for x in range(18,24):
        downList.append(tuple(list[x]))
    for x in range(24,30):
        leftList.append(tuple(list[x]))
    for x in range(30,36):
        backList.append(tuple(list[x]))
        
    file.close()
    colorList = []
    colorList.append(upList)
    colorList.append(rightList)
    colorList.append(fwdList)
    colorList.append(downList)
    colorList.append(leftList)
    colorList.append(backList)
    return colorList



#print("R: " + str(pxl[2]) + "\tG: " + str(pxl[1]) + "\tB: " + str(pxl[0]))

