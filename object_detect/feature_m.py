import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    
    
    
puff = cv2.imread('img/puff.jpg', 0)    
cereals = cv2.imread('img/many_carals.jpg',0)


sift = cv2.xfeatures2d.SIFT_create()

kp1,descrip1 = sift.detectAndCompute(puff, None)
kp2,descrip2 = sift.detectAndCompute(cereals,None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(descrip1,descrip2, k=2)

good = []

for match1,match2 in matches:
    
    if match1.distance < 0.75*match2.distance:
        good.append([match1])

sift_match = cv2.drawMatches(puff,kp1,cereals,kp2,good,None,flags=2)

display(sift_match)
