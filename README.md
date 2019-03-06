# Handwritten-digits-recognition

This project is made up of two parts, firstly digits localization, secondly recognition.

Localization

Use OpenCV to preprocess data by following steps:

get inputs ->  convert into Grayscale ->  Binariztion ->  Edge detection 
->  Finding contour ->  Remove noise ->  Extract ROI ->  Resize to (28,28)

Recognition

Training MNIST classification model, input each individual digit
