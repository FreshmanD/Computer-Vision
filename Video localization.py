import numpy as np
import cv2 as cv
way = input("loading method: ")
print('the video stream is from: ', way)

if way == 'CAM':
    name = 0
elif way == 'FILE':
    name = input('file name: ')
else:
    name = 0
cap = cv.VideoCapture(name)

while(True):
    ret, img = cap.read()
##
##    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
##    lower_white = np.array([0,0,221])
##    upper_white = np.array([180,30,255])
##    lower_black = np.array([0,0,0])
##    upper_black = np.array([180,255,46])
##    mask = cv.inRange(hsv,lower_white, upper_white)
##    mask1 = cv.inRange(hsv,lower_black, upper_black)
##    mask = mask
##    canvas = np.ones((img.shape[0],img.shape[1],3),np.uint8)
##    res = cv.bitwise_and(img,img, mask = mask)
##    cv.imshow('res',res)
##    gray = cv.cvtColor(res,cv.COLOR_HSV2BGR)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray,(3,3),0)
    thresh = cv.adaptiveThreshold(blur,127,1,1,11,2)
    edge = cv.Canny(thresh,70,70)

    cnt1,hierarchy1 = cv.findContours(edge,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cnts1 = sorted(cnt1, key = cv.contourArea, reverse=True)

    canvas = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    IAP = cv.drawContours(edge,cnts1,-1,(255,255,255),1)

    cnt2,hierarchy2 = cv.findContours(edge,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts2 = sorted(cnt2, key = cv.contourArea, reverse=True)
    length2 = len(cnts2)
    #cnts2 = cnts2[int(0.02*length2):int(0.4*length2)]
    cnts3 = []
    aspect_ration1 = 0
    for i in range(len(cnts2)):
        x1,x2,x3,x4 = False,False,False,False
        area = cv.contourArea(cnts2[i])
        if area > 250:
            x3 = True
        if(len(cnts2[i]) >= 5):
            x,y,w,h = cv.boundingRect(cnts2[i])
            aspect_ration1 = float(w)/h
            _,_,angle1 = cv.fitEllipse(cnts2[i])

            if (3 > aspect_ration1 >= 0.15):
                x1 = True
            if not (100 < angle1 < 85):
                x2 = True
            #if 2.25 > aspect_ration1:
            #    x1 = True
            #if not(95 > angle1 > 75):
            #    x2 = True
            if x1 and x2 and x3:
                cnts3.append(cnts2[i])
    count = 0            
    for i in range(len(cnts3)):
        x,y,w,h = cv.boundingRect(cnts3[i])
        ROI = img[y:y+h+1,x:x+w+1]
        #cv.imshow('ROI',ROI)
        #cv.waitKey(0)
        #roi = cv.resize(ROI,(28,28))
        #title = 'ROI' + str(i+1) + '.jpg'
        #cv.imwrite(title,roi)
        IAP1 = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        if(IAP1.any()):
            count = 1

    if(count == 0):
        cv.imshow('IAP1',img)
        #cv.waitKey(30)
    else:
        cv.imshow('IAP1',IAP1)
        #cv.waitKey(30)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
