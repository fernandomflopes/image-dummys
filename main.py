import cv2 as cv
import time
import os
import numpy as np

from random import randint

def new_name():
    return str(time.time()).replace(".", "") + ".png"

def generate_image(path, image_name):
    img = cv.imread(os.path.join(media_path, image_name))

    for i in img:
        for j in i:
            j[randint(0, 2)] = randint(0, 255)

    cv.imwrite(os.path.join(path, new_name()), img)    
    return img

def generate_noise_image(path):
    img = np.zeros((256,256,3), np.uint8)
    
    for i in img:
        for j in i:
            j[0] = randint(0, 255)
            j[1] = randint(0, 255)
            j[2] = randint(0, 255)

    cv.imwrite(os.path.join(path, new_name()), img) 

    return img 

def get_media_path():
    media_path = os.path.abspath("media")
    if not os.path.exists(media_path):
        os.mkdir(media_path)
    return media_path


if __name__ == '__main__':
    import sys

    times = 1   
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        if int(sys.argv[2]) > 0:
            times = int(sys.argv[2])

    for i in range(0, times):
        generate_noise_image(get_media_path())
