import librosa
import librosa.display
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import warnings
import random as rd
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

def rainbow(image):
    new_image = np.zeros((300, image.shape[1], 3), dtype = np.uint8)
    for i in range(300):
        for j in range(new_image.shape[1]):
            if(image[i, j] == 0):
                new_image[i, j] = (0, 0, 0)
            else:
                f2 = rd.randint(0, 255)
                f1 = rd.randint(0, 255)
                f3 = rd.randint(0, 255)
                new_image[i, j] = (f1, f2, f3)
    return(new_image)

def get_num(audio_file):
    y1, sr1 = librosa.load(audio_file, sr=None)

    
    n_fft = 2048  
    hop_length = 512  

    spec_m1 = librosa.feature.melspectrogram(y=y1, sr=sr1, n_fft=n_fft,
                                        hop_length=hop_length, fmax=22000)

    spec_m1 = librosa.power_to_db(spec_m1)


    spec_m1 = cv.normalize(spec_m1, None, 0, 255, cv.NORM_MINMAX)


    spec_m1 =spec_m1.astype(np.uint8)
    if(spec_m1.mean() > 93):
        return(1)
    else:
        return(2)


sum = 0
total_files = 20
audio_files = [] #add paths here

for i in range(total_files):
    audio_file_path = audio_files[i]
    sum = sum + get_num(audio_file_path)
    
sum = str(sum)
num_digs = int(len(sum))

image = np.zeros((300, num_digs*200), dtype=np.uint8)

shuru = 0

for i in range(len(sum)):
    foo = int(sum[i])
    add_num(image, shuru, foo)
    shuru = shuru + 200

image = rainbow(image)

cv.imshow('img', image)

cv.waitKey(0)
