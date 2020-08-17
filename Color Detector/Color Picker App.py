import cv2
import numpy as np

#What's next is to figure out how to convert the color names for each square, to kociemba-readable strings
#Use the middle square (U5, R5 etc) to define the base of each face


#Compares color from parameter to cube colors, for matching colors; Returns color
def findColor(img, coordinates):
    red, blue, green, orange, yellow, white = [0,0,255], [255,0,0], [0,255,0], [0,128,255], [0,255,255], [255,255,255]  #Color RGB values
    img = cv2.imread(img)
    color = img[coordinates] #outputs as [B G R]

    #Calculates the difference between RGB values
    RC = abs(color[0] - red[0]) + abs(color[1] - red[1]) + abs(color[2] - red[2])
    BC = abs(color[0] - blue[0]) + abs(color[1] - blue[1]) + abs(color[2] - blue[2])
    GC = abs(color[0] - green[0]) + abs(color[1] - green[1]) + abs(color[2] - green[2])
    OC = abs(color[0] - orange[0]) + abs(color[1] - orange[1]) + abs(color[2] - orange[2])
    YC = abs(color[0] - yellow[0]) + abs(color[1] - yellow[1]) + abs(color[2] - yellow[2])
    WC = abs(color[0] - white[0]) + abs(color[1] - white[1]) + abs(color[2] - white[2])

    mini = min(RC,BC,GC,OC,YC,WC) #finds the smallest difference
    
    #Matches the smallest difference in RGB to corresponding color (best match)
    Dict = {'red' : RC, 'blue' : BC, 'green' : GC, 'orange' : OC, 'yellow' : YC, 'white':WC} 
    for x,y in Dict.items():
        if y == mini:
            return(x)

img = 'cube.jpg'

#Coordinates of each square on the respective images
f1 = findColor(img, (0,0))
f2 = findColor(img, (0,0))
f3 = findColor(img, (0,0))
f4 = findColor(img, (0,0))
f5 = findColor(img, (0,0))
f6 = findColor(img, (0,0))
f7 = findColor(img, (0,0))
f8 = findColor(img, (0,0))
f9 = findColor(img, (0,0))

r1 = findColor(img, (0,0))
r2 = findColor(img, (0,0))
r3 = findColor(img, (0,0))
r4 = findColor(img, (0,0))
r5 = findColor(img, (0,0))
r6 = findColor(img, (0,0))
r7 = findColor(img, (0,0))
r8 = findColor(img, (0,0))
r9 = findColor(img, (0,0))

d1 = findColor(img, (0,0))
d2 = findColor(img, (0,0))
d3 = findColor(img, (0,0))
d4 = findColor(img, (0,0))
d5 = findColor(img, (0,0))
d6 = findColor(img, (0,0))
d7 = findColor(img, (0,0))
d8 = findColor(img, (0,0))
d9 = findColor(img, (0,0))

b1 = findColor(img, (0,0))
b2 = findColor(img, (0,0))
b3 = findColor(img, (0,0))
b4 = findColor(img, (0,0))
b5 = findColor(img, (0,0))
b6 = findColor(img, (0,0))
b7 = findColor(img, (0,0))
b8 = findColor(img, (0,0))
b9 = findColor(img, (0,0))

l1 = findColor(img, (0,0))
l2 = findColor(img, (0,0))
l3 = findColor(img, (0,0))
l4 = findColor(img, (0,0))
l5 = findColor(img, (0,0))
l6 = findColor(img, (0,0))
l7 = findColor(img, (0,0))
l8 = findColor(img, (0,0))
l9 = findColor(img, (0,0))

u1 = findColor(img, (0,0))
u2 = findColor(img, (0,0))
u3 = findColor(img, (0,0))
u4 = findColor(img, (0,0))
u5 = findColor(img, (0,0))
u6 = findColor(img, (0,0))
u7 = findColor(img, (55,55)) 
u8 = findColor(img, (100,25))
u9 = findColor(img, (150,180))



print(u6)
print(u7)
print(u8)
print(u9)
x = input()
