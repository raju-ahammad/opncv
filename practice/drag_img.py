import numpy as np
 
import cv2

drawing = True
ix = -1
iy = -1

def rectangle(event,x,y,flags,param):
    
    global drawing, ix,iy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)         
        
        



cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img',rectangle)


img = np.zeros(shape=(512,512,3), dtype=np.int8)
while True:
    
    cv2.imshow('my_img',img)
    if cv2.waitKey(1) & 0xFF==27:
        break

        
cv2.destroyAllWindows()        