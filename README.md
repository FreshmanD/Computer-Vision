# Computer Vision Project

### HandWritten digit locolization and recognition

* **Locolization**
Utilize OpenCV libary to extract image unique feature for better precise locolization.
<br>

    Image processing step:
    * Grayscale raw image
    * Binariztion 
    * Edge detection
    * Extract contour 
    * Remove noise
    * Calculate ROI
<br>

* **Recognition**
Design a simple neural network with just 2 dense layer

<img src= width="300">

### YOLO object recognition

YOLO (You Only Look Once) is an object recognition algorithm. 

The standard YOLO model is trained using COCO dataset with 80 kinds of objects.

In this project, the YOLO model is further trained using a new dataset, [MCIndoor 20000](https://github.com/bircatmcri/MCIndoor20000), to recognize **door**.

