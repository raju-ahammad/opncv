import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    #convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    #define range blue color in hsv
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    #Threshold the hsv img to get only blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    #original img 
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('result', result)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()        
    