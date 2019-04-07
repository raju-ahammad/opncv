import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/girl.jpeg', 1)
cv2.namedWindow('girl', cv2.WINDOW_NORMAL) #window resize

cv2.imshow('girl', img)

k = cv2.waitKey(0) & 0xFF
# esc for stop window
if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):   # wait for s key to save or esc
    cv2.imwrite('img/beutygirl.png', img)
    cv2.destroyAllWindows()


# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
