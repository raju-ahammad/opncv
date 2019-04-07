import numpy as np
import cv2

#img = np.zeros((512,512,3), np.int8)
img1 = np.zeros((512,512,3), np.int8)
cv2.namedWindow('img', cv2.WINDOW_NORMAL) #window resize

#cv2.line(img, (0,0), (511,511), (255,0,0), 5)
cv2.rectangle(img1, (200,30), (500,200), (34,139,34), -1)
cv2.circle(img1,(350,120), 63, (139,0,0), -1)
cv2.imshow('img', img1)
cv2.waitKey(0) & 0xFF==27
cv2.destroyAllWindows()
