import cv2
img = cv2.imread('img/tony.jpg')
while True:
    cv2.imshow('Tony', img)
    # waiting for at least 1 mili sec  AND press esc for closed
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
       