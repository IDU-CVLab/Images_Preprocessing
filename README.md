# Image Processing for COV19-CT-DB Database work

The work intend to appropriately segment CT scan images in the COV19-CT-DB database and filter out uppermost and lower most slices of the CT volumetric image before classification. The work aims at improving quantitative results on the given dataset. 
# Guided GRad-Cam VIsualization <br/>
In an attempt to understand how our mode at https://github.com/IDU-CVLab/COV19D/blob/main/COV19-CT-DB-CNN-model.py classifies the images in the COV19-CT-DB database a guided crag-cam class was used on the last convulutional layer. A non-covid image of the dabase is shown bellow along with the heatmap and the overlaping of the heatmap on the image.
<p align="center">
  <img src="https://github.com/IDU-CVLab/Images_Preprocessing/blob/main/Figures/CORRECT-COVID5.png" /> <br/>
  Taken from COV19-CT-DB Database (COVID19 Case) <br/>
  Correctly Classified COVID CT slice 
</p>      
<br/>

# Images_Preprocessing
#1. segmentation and cropping.py <br/>
The code uses python open-cv for gussian blurring, cropping and histogram segmentation of medical images. The code is an attempt to segment lung CT scan images.

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
