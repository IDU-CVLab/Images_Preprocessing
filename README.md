# Image Processing for COV19-CT-DB Database work

The work intends to appropriately segment CT scan images in the COV19-CT-DB database and filter out uppermost and lower most slices of the CT volumetric images before classification. The work aims at improving quantitative results on the given dataset. 
# Guided GRad-Cam Visualization <br/>
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

The original Image looks like:
<p align="center">
  <img src="https://github.com/IDU-CVLab/Images_Preprocessing/blob/main/Figures/original.png" /> <br/>
  Taken from COV19-CT-DB Database (COVID19 Case)
</p>      
<br/>

The resulting image looks as follows:
<p align="center">
  <img src="https://github.com/IDU-CVLab/Images_Preprocessing/blob/main/Figures/cropped%20and%20segmented.png" />
</p>      
<br/>

## 1. Region Of Interest cropping <br/>
The code is an attempt to achieve high accuracy with a model by training it on representative images or images with region of interest. with that the CT images were cropped to include the right lung from the CT scan image using opencv version 4. The region of interest is represented simply by a static rectangle. The region of interest in the image is shows in the white rectangle (size of 240x157) as follows: <br/>
<p align="center">
  <img src="https://github.com/IDU-CVLab/Images_Preprocessing/blob/main/Figures/ROI%20static%20rectangular%20crop.png" /> <br/>
  Taken from COV19-CT-DB Database (COVID19 Case)
</p>      
<br/>

