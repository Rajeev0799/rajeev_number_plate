
###upload file in google colab
from google.colab import files
uploaded = files.upload()

########import necessary packages and files########################
import cv2
import  imutils
from google.colab.patches import cv2_imshow
import numpy as np


##########PreProcessing########
image = cv2.imread("car2.jpg")##read imahe
cv2_imshow(image)##print image
grayim = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)##convert color to gray
print(grayim.shape)
###########Resize the original if it is 500W###################
ht,wdh = grayim.shape
ratio = float(wdh) / ht
if (wdh > 500):
  wdh = 500
  ht = round(wdh / ratio)
grayim= imutils.resize(grayim, width=wdh,height=ht)
#cv2_imshow(img)
#grayim = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(grayim)
r,thim=cv2.threshold(grayim,128,255,cv2.THRESH_OTSU)#####Apply otsu method to find binary of original image
cv2_imshow(thim)

##########Number Plate detection##########
###########
#########import necessary ############
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches

label_im = measure.label(thim)##Label the image refgions using measure
cv2_imshow(label_im)
##find the dimensions according to assumptions
Numberplate_dims = (0.08*label_im.shape[0], 0.2*label_im.shape[0], 0.15*label_im.shape[1], 0.4*label_im.shape[1])
min_height, max_height, min_width, max_width = Numberplate_dims
rectangle_objects_coords = []
rectangle_objects = []

min_height, max_height, min_width, max_width = Numberplate_dims
rectangle_objects_coords = []
rectangle_objects = []

fig, (ax1) = plt.subplots(1)
ax1.imshow(grayim, cmap="gray")
#For each labelled connected region
for region in regionprops(label_im):
    print('hai')
    if region.area < 50: #avoid region areais less than 50
      continue
      # Find the coordinates of bounding box using bbox
    min_row, min_col, max_row, max_col = region.bbox
    print(min_row, min_col, max_row,max_col)

    region_height = max_row - min_row
    region_width = max_col - min_col
    print(region_height, region_width)
    ###############  find rectangle regions############    
    if region_height >= min_height and region_width >= min_width and region_width > region_height:
          print("hello")
        #########Extract coordinates of the rectangle regions###########
          rectangle_objects.append(thim[min_row:max_row,min_col:max_col])
          rectangle_objects_coords.append((min_row, min_col,max_row, max_col))
          rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row, edgecolor="blue",linewidth=3, fill=False)
          ###########draw line
          ax1.add_patch(rectBorder)
            
print(min_height, max_height, min_width, max_width)
plt.show()###show the image with rectangle regions
######Conclude the rectangle region with maximum white pixels as the number plate region
cc=0
av=[]
for ob in rectangle_objects:
            height, width = ob.shape
            print(width)
            Number_plate = []
            white_pixels = 0
            for c in range(width):
                white_pixels += sum(ob[:, c])
            av.append(float(white_pixels) / width)
highest_avg=max(av)
cc=0
for ob in rectangle_objects:
  if av[cc] >= highest_avg:
                print('hai')
                Number_plate = ob
                cv2_imshow(Number_plate)
  cc+=1
  
  
  ############To install pytesseract in colab
  !sudo apt install tesseract-ocr
!pip install pytesseract

import pytesseract as tess

cv2_imshow(Number_plate)
Vehicle_Num = tess.image_to_string((Number_plate))#, lang='eng')
print ("Vehicle number is  ",Vehicle_Num)
