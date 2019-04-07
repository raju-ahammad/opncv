import numpy as np
import cv2

# create funtion 
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),80,(255,255,255),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)

cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img', draw_circle)


# showing img with open cv

img = np.zeros(shape=(512,512,3), dtype=np.int8)

while True:
    cv2.imshow("my_img", img)
    if cv2.waitKey(20) & 0xFF==27:
        break
 
cv2.destroyAllWindows()
