# Image Processing for COV19-CT-DB Database work

The work intend to appropriately segment CT scan images in the COV19-CT-DB database and filter out uppermost and lower most slices of the CT volumetric image before classification. The work aims at improving quantitative results on the given dataset. 

# Images_Preprocessing
segmentation and cropping.py code uses python open-cv for gussian blurring, cropping and histogram segmentation of medical images. The code is an attempt to segment lung CT scan images. 

The original Image looks like:
<p align="center">
  <img src="https://github.com/kenanmorani/Images_Preprocessing/blob/main/FIgures/original.png" /> <br/>
  Taken from COV19-CT-DB Database 
</p>      
<br/>

The resulting image looks as follows:
<p align="center">
  <img src="https://github.com/kenanmorani/Images_Preprocessing/blob/main/FIgures/cropped%20and%20segmented.png" />
</p>      
<br/>
