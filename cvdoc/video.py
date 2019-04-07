import numpy as np
import cv2

cap = cv2.VideoCapture('vid.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('new.mp4',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()



# import numpy as np
# import cv2
#
# #cap = cv2.VideoCapture('vid.mp4')
# cap = cv2.VideoCapture('vid.mp4')
#
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
#
# while (cap.isOpened()):
#     # capture frme by frame
#     ret, frame =  cap.read()
#
#     if ret == True:
#         #frame = cv2.flip(frame, 0)
#
#         output.write(frame)
#
#     #oparation frame came here
#     #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#
#     # disply the resulting frmae
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
#
#
#
# cap.release()
# output.release()
# cv2.destroyAllWindows()
