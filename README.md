# Visualization and Image Processing for COV19-CT-DB Database Work

The work intends to appropriately segment CT scan images in the COV19-CT-DB database and filter out uppermost and lowermost slices of the CT volumetric images before classification. The work aims at improving quantitative results on the given dataset. 
# Guided GRad-Cam Visualization <br/>
The code is "Guided-GRad-Cam.py": <br/>
In an attempt to understand how our mode at https://github.com/IDU-CVLab/COV19D/blob/main/COV19-CT-DB-CNN-model.py classifies the images in the COV19-CT-DB database, a guided grad-cam class was used on the last convulutional layer. A covid image from the dabase is shown bellow along with the heatmap and the overlaping of the heatmap on the image.
<p align="center">
  <img src="https://github.com/IDU-CVLab/Images_Preprocessing/blob/main/Figures/CORRECT-COVID5.png" /> <br/>
  Taken from COV19-CT-DB Database (COVID19 Case) <br/>
  Correctly Classified COVID CT slice 
</p>      
<br/>

### REFERENCES: <br>
https://stackoverflow.com/questions/66911470/how-to-apply-grad-cam-on-my-trained-model {Last Access 13.12.2021}

# Images Preprocessing
## 1. segmentation and cropping <br/>
The code 'cropping-and-segmentation.py' uses python open-cv for gussian blurring, cropping and histogram segmentation of medical images. The code is an attempt to segment lung CT scan images.

The original images look as follows:
<p align="center">
  <img src="https://github.com/kenanmorani/Images_Preprocessing/blob/main/FIgures/original.png" />
</p>      
<br/>

The resulting image looks as follows:
<p align="center">
  <img src="https://github.com/kenanmorani/Images_Preprocessing/blob/main/FIgures/cropped%20and%20segmented.png" />
</p>      
<br/>

### REFERENCES: <br>
https://datacarpentry.org/image-processing/07-thresholding/ {Last Access 15.12.2021}

## 2. Region of Interest cropping <br/>
The code 'Rectangular-cropping.py' is an attempt to achieve high accuracy with a model by training it on representative images or images with region of interest. with that the CT images were cropped to include the left and right lung from the CT scan image using opencv version 4. The region of interest is represented simply by a static rectangle. The region of interest in the image is shown in the white rectangle (size of 227x300) as follows: <br/>
<p align="center">
  <img src="https://github.com/kenanmorani/Images_Preprocessing/blob/main/FIgures/rectangular-cropping.jpg" /> <br/>
  Taken from COV19-CT-DB Database
</p>      
<br/>

### REFERENCES: <br/>
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html {Last Access 15.12.2021} <br/>
https://stackoverflow.com/questions/56467902/select-a-static-roi-on-webcam-video-on-python-opencv {Last Access 15.12.2021} <br/>
https://stackoverflow.com/questions/15341538/numpy-opencv-2-how-do-i-crop-non-rectangular-region {Last Access 15.12.2021} <br/>


## 3. Countor Images Cropping 
The code 'COV19D_CT_images_Processing_Using_Contour_Cropping.ipynb' is an an attempt to segment and highlight region of interests in the images, this code applies a function to crop Region of Interests on the CT images using open-cv. Results of cropping can be seen in the code on one of the CT images- a central slice.

## 4. Region based Image Segementation
The code 'Region-Based_Image-Segmentation_full-CT-SCAN.ipynb'. This code used the region based image segmentation method [here](https://github.com/kenanmorani/Images_Preprocessing/blob/main/Region_Based_Segmentation.ipynb) at to be run on full CT scan of nnon-Covid to replace the slices with masks. 

