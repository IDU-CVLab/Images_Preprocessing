#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:45:19 2021

@author: idu

REFERENCES:
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
https://stackoverflow.com/questions/56467902/select-a-static-roi-on-webcam-video-on-python-opencv
https://stackoverflow.com/questions/15341538/numpy-opencv-2-how-do-i-crop-non-rectangular-region
"""""
import cv2
file_path = '/home/idu/Desktop/COV19D/train/covid/ct_scan_3/20.jpg'
#img=load_img(file_path, color_mode='grayscale', target_size=(512,512))
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

##############33https://learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
# Selecting Static REctangular ROI
im = img
# Select ROI
r = cv2.selectROI(im)
# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
imCrop = np.expand_dims(imCrop, axis=2)
imCrop = array_to_img (imCrop)
imCrop.save("/home/idu/Desktop/COV19D/1.jpg",'JPEG')


cv2.imshow("/home/idu/Desktop/COV19D/", imCrop)
cv2.waitKey(0)