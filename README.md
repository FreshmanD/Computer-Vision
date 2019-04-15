# Handwritten-digits-recognition

This project is made up of two parts, firstly digits localization, secondly recognition.

Localization

1. Imagedetection.py
Use OpenCV to preprocess data by following steps:

Get inputs ->  convert into Grayscale ->  Binariztion ->  Edge detection 
->  Finding contour ->  Remove noise ->  Extract ROI ->  Resize to (28,28)

2. Videodetection.py
Provide two video capture methods (file or camera). Localization technique is same as Image detection.

Recognition

1. Videorecognition.py
Training MNIST classification model, based on Videodetection.py, modify ROI extraction technique to get better recognition result.
