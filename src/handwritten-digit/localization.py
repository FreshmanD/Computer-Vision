import numpy as np
import cv2 as cv

img = cv.imread(img_path)

# Convert raw_img to grayscale_img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Remove big noise 
blur = cv.GaussianBlur(gray, (9, 9), 20)

# Extract contour
ret,thresh = cv.threshold(blur, 127, 255, 0)
edge = cv.Canny(thresh, 100, 200)
# Remove small noise
kernel = np.ones((3,3), np.uint8)
dilation = cv.dilate(edge, kernel, iterations = 1)
erosion = cv.erode(dilation, kernel, iterations = 1)
cnt1, hierarchy1 = cv.findContours(erosion, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnts1 = []
max_temp1 = 0
for i in range(len(cnt1)):
    temp = cv.contourArea(cnt1[i])
    if temp > max_temp1:
        max_temp1 = temp
    
for i in range(len(cnt1)):
    temp = cv.contourArea(cnt1[i])
    if temp > 0.1 * max_temp1:
        cnts1.append(cnt1[i])

# Find contour's contour         
IAP = cv.drawContours(erosion, cnts1, -1, (255, 255, 255), 1)
cnt2, hierarchy2 = cv.findContours(erosion, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts2 = []
max_temp2 = 0
for i in range(len(cnt2)):
    temp = cv.contourArea(cnt2[i])
    if temp > max_temp2:
        max_temp2 = temp
        
for i in range(len(cnt2)):
    temp = cv.contourArea(cnt2[i])
    if temp > 0.04 * max_temp2:
        cnts2.append(cnt2[i])

# Set threshold to select the final candidate 
cnts3 = []
for i in range(len(cnts2)):
    x1, x2 = False, False
    x, y, w, h = cv.boundingRect(cnts2[i])
    aspect_ration = float(w) / h
    _, _, angle = cv.fitEllipse(cnts2[i])

    if 2.5 > aspect_ration and not 0.88 < aspect_ration < 1.12:
        x1 = True
    if not (100 > angle > 70):
        x2 = True
    if x1 and x2:
        cnts3.append(cnts2[i])

for i in range(len(cnts3)):
    x, y, w, h = cv.boundingRect(cnts3[i])
    ROI = thresh[y - 10 : y + h + 25, x - 10 : x + w + 25]
    IAP = cv.rectangle(self.img, (x, y), (x + w + 5, y + h + 5), (0, 255, 0), 2)
cv.imshow('Localize Result',IAP)
k = cv.waitKey(0)
# wait for ESC key to exit
if k == 27:
    cv.destroyAllWindows()
