# Computer Vision Project

### HandWritten digit locolization and recognition

**Locolization**
Use OpenCV libary to extract image unique feature for better precise locolization.

Image processing step:
* Grayscale raw image
* Binariztion 
* Edge detection
* Extract contour 
* Remove noise
* Calculate ROI

**Recognition**
Design a simple neural network with just 2 dense layer

<img src="https://github.com/FreshmanD/Computer-Vision/blob/master/img/localize_result.png?raw=true" width="500">

### YOLO object recognition

YOLO (You Only Look Once) is an object recognition algorithm. 

The standard YOLO model is trained using COCO dataset with 80 kinds of objects.

In this project, the YOLO model is further trained using a new dataset, [MCIndoor 20000](https://github.com/bircatmcri/MCIndoor20000), to recognize **door**.

<img src="https://github.com/FreshmanD/Computer-Vision/blob/master/img/yolo_street_recognize.png?raw=true" width="500">

<img src="https://github.com/FreshmanD/Computer-Vision/blob/master/img/yolo_door_recognize.jpg?raw=true" width="300">