import numpy as np
import cv2 as cv
import keras
import localization

# Select video method
way = input("Loading method: ")
print('the video stream is from: ', way)

if way == 'CAM':
    name = 0
elif way == 'FILE':
    name = input('file name: ')
else:
    name = 0

cap = cv.VideoCapture(name)
model = keras.models.load_model('model.h5')

while(True):
    ret, img = cap.read()
    # Successfully load img
    if ret == True:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (3, 3), 0)
        ret, thresh = cv.threshold(blur, 150, 255, cv.THRESH_BINARY_INV)
        edge = cv.Canny(thresh, 70, 70)

        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
        dilated = cv.dilate(thresh, kernel, iterations = 2)
        cnt2, hierarchy1 = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        cnts3 = []
        aspect_ration1 = 0
        for i in range(len(cnt2)):
            x1, x2, x3 = False, False, False
            area = cv.contourArea(cnt2[i])
            if area > 100:
                x3 = True
            if(len(cnt2[i]) >= 5):
                x, y, w, h = cv.boundingRect(cnt2[i])
                aspect_ration1 = float(w) / h
                _, _, angle1 = cv.fitEllipse(cnt2[i])

                if 3 > aspect_ration1:
                    x1 = True
                if angle1 > 100 or angle1 < 30:
                    x2 = True
                if x1 and x2 and x3:
                    cnts3.append(cnt2[i])

        #           
        found = False           
        for i in range(len(cnts3)):
            x, y, w, h = cv.boundingRect(cnts3[i])
            ROI = thresh[y : y + h + 1, x : x + w + 1]
            size = ROI.shape
            if size[0] * size[1] > 0:
                ROI = cv.resize(ROI, (28, 28))
                ROI = cv.copyMakeBorder(ROI, 10, 10, 10, 10, cv.BORDER_CONSTANT, value = [0, 0, 0])
                ROI = cv.resize(ROI, (28, 28))

                canvas = np.array(ROI)
                canvas = canvas.reshape(1, 28 * 28)
                canvas = canvas.astype('float32') / 255
                result = model.predict_classes(canvas)
                proba = model.predict_proba(canvas)
                if max(proba[0]) >= 1.5e-01:
                    font = cv.FONT_HERSHEY_SIMPLEX
                    cv.putText(img, str(result[0]), (x, y - 10), font, 1, (255, 0, 0), 2)
                    IAP = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if(IAP1.any()):
                count = True

        if not found:
            cv.imshow('No digit found', img)
        else:
            cv.imshow('Recognize result', IAP)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv.destroyAllWindows()
cap.release()
