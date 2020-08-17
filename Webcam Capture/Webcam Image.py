import time
import cv2

camera_port = 0
camera = cv2.VideoCapture(camera_port)
#camera2 = cv2.VideoCapture(1)

print("Pic")
time.sleep(0.4)  # If you don't wait, the image will be dark
return_value, image = camera.read()
cv2.imwrite("opencv.png", image)

#return_value, image = camera2.read()
#cv2.imwrite("opencv2.png", image)

del(camera)  # so that others can use the camera as soon as possible
#del(camera2)
