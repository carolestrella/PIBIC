import cv2
import imutils
import imutils.perspective as persp
import scipy.spatial.distance as dist
import numpy as np
import os
import matplotlib.pyplot as plt
from __future__ import print_function
import argparse
import random as rng

from google.colab import drive
drive.mount("/content/drive",force_remount=True)

path = '/content/drive/MyDrive/kimia216/bird/bird02.png'
img = cv2.imread(path)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.show()

def thresh_callback(val):
    threshold = val
    # Detect edges using Canny
    canny_output = cv2.Canny(rgb_img, threshold, threshold * 2)

    # Find contours
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)

    # Show in a window
    plt.imshow(drawing)
    plt.show()

    #AREA
    area = cv2.contourArea(cnt)
    print('\n' + 'AREA:')
    print(area)

    #PERIMETER
    perimeter = cv2.arcLength(cnt,True)
    print('\n' +'PERIMETER:')
    print(perimeter)

    #CONVEX HULL
    hull = cv2.convexHull(cnt)
    print('\n' +'CONVEX HULL:')
    print(hull)

    #ASPECT RATIO
    x,y,w,h = cv2.boundingRect(cnt)
    aspect_ratio = float(w)/h
    print('\n' +'ASPECT RATIO:')
    print(aspect_ratio)

    #EXTENT
    x,y,w,h = cv2.boundingRect(cnt)
    rect_area = w*h
    extent = float(area)/rect_area
    print('\n' +'EXTENT:')
    print(extent)

    #SOLIDITY
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area
    print('\n' +'SOLIDITY:')
    print(solidity)

    #EQUIVALENT DIAMETER
    equi_diameter = np.sqrt(4*area/np.pi)
    print('\n' +'EQUIVALENT DIAMETER:')
    print(equi_diameter)

    #ORIENTATION
    (x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
    print('\n' +'ORIENTATION:')
    print(angle)

thresh_callback(100)