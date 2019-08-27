# rajeev_number_plate
The solution for License plate detection. Comprises of 3 major phases 1. Preprocessing, 2. Number plate detection using connected components analysis 3. Character recognition using tesseract
The code was implemented in google colab.

It was developed using Python 3 notebook
Importing Necessary packages and files:
import cv2
import  imutils
from google.colab.patches import cv2_imshow
import numpy as np
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pytesseract as tess

Installing pytesseract in google colab:
!sudo apt install tesseract-ocr
!pip install pytesseract

###To upload files in google colab
from google.colab import files
uploaded = files.upload()
