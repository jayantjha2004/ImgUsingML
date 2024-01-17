import cv2 as cv
import caer
import warnings
import numpy as np
warnings.filterwarnings('ignore')

height = 300
radius = 25

def add_num(img, shuru, num):
    if(num == 1):
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
    elif(num == 2):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
    elif(num == 3):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
    elif(num == 8):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 200), radius = radius, color = 255, thickness = -1)
    elif(num == 9):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50,  100), radius = radius, color = 255, thickness = -1)
    elif(num == 6):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 200), radius = radius, color = 255, thickness = -1)
    elif(num == 5):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50,  100), radius = radius, color = 255, thickness = -1)
    elif(num == 0):
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 200), radius = radius, color = 255, thickness = -1)
    elif(num == 7):
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 50), radius = radius, color = 255, thickness = -1)
    elif(num == 4):
        cv.circle(img, (shuru + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (shuru + 50, 100), radius = radius, color = 255, thickness = -1)

n = int(input())
n = 2**n  -1

n = str(n)

num_digs = int(len(n))

image = np.zeros((300, num_digs*200), dtype=np.uint8)

shuru = 0

for i in range(len(n)):
    foo = int(n[i])
    add_num(image, shuru, foo)
    shuru = shuru + 200
    

cv.imshow('img', image)

cv.waitKey(0)












