import cv2
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
hieght = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

record = cv2.VideoWriter('myvideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), 10,(width, hieght))

while True:
    
    ret, frame =  cap.read()
    
    record.write(frame)
    
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
record.release()
cv2.destroyAllWindows()