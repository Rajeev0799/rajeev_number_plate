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


References:
1.	Patel, Smt. Chandaben Mohanbhai, Dipti Shah , Automatic Number Plate Recognition System (ANPR): A Survey Chirag, International Journal of Computer Applications (0975 – 8887) Volume 69– No.9, May 2013
2.	K.M. Sajjad, Automatic License Plate Recognition using Python and OpenCV
3.	Hanit Karwal#1, Akshay Girdhar, Vehicle Number Plate Detection System for Indian Vehicles, 2015 IEEE, DOI 10.1109/CICT.2015.13
4.	https://github.com/femioladeji/License-Plate-Recognition-Nigerian-vehicles
5.	https://medium.com/datadriveninvestor/license-plate-detector-code-build-and-deploy-790579a18402
6.	https://github.com/apoorva-dave/LicensePlateDetector?source=post_page-----790579a18402----------------------
7.	https://towardsdatascience.com/automatic-license-plate-detection-recognition-using-deep-learning-624def07eaaf
8.	https://github.com/anuj-badhwar/Indian-Number-Plate-Recognition-System/blob/master/main.py

