#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 01:34:25 2021

@author: idu
"""

import skimage
from skimage import color, filters
import numpy as np
import os, glob
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras import layers, models
from tensorflow.keras import activations
from tensorflow.keras.models import Sequential
from termcolor import colored  

import visualkeras
from tensorflow.python.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, ZeroPadding2D
from collections import defaultdict

from PIL import ImageFont

from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img

import pandas as pd

import csv
from sklearn.utils import class_weight 
from collections import Counter


t = 0.4 #Histogram Threshold
#### Cropping right-lung as an ROI and removing upper and lowermost of the slices 
count = []
folder_path = '/home/idu/Desktop/COV19D/validation/covid' 
#Change this directory to the directory where you need to do preprocessing for images
#Inside the directory must folder(s), which have the images inside them
for fldr in os.listdir(folder_path):
        sub_folder_path = os.path.join(folder_path, fldr)
        for filee in os.listdir(sub_folder_path):
            file_path = os.path.join(sub_folder_path, filee)
            img = cv2.imread(file_path)
            #Grayscale images
            img = skimage.color.rgb2gray(img) 
            # First cropping an image
            #%r = cv2.selectROI(im) 
            #Select ROI from images before you start the code 
            #Reference: https://learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
            #{Last access 15th of Dec, 2021}
            # Crop image using r
            img_cropped = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] 
            # Thresholding and binarizing images
            # Reference: https://datacarpentry.org/image-processing/07-thresholding/
            #{Last access 15th of Dec, 2021}
            # Gussian Filtering
            img = skimage.filters.gaussian(img_cropped, sigma=1.0)
            # Binarizing the image
            img = img < t
            count = np.count_nonzero(img)
            #print(count)
            if count > 2000:
             img_cropped = np.expand_dims(img_cropped, axis=2)
             img_cropped = array_to_img (img_cropped)
               # Replace images with the image that includes ROI
             img_cropped.save(str(file_path), 'JPEG')
             #print('saved')
            else:
                # Remove non-representative slices
             os.remove(str(file_path))
             #print('removed')
             # Check that there is at least one slice left
            if not os.listdir(str(sub_folder_path)):
              print(str(sub_folder_path), "Directory is empty")
            count = []
