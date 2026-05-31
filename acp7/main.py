import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

(h, w) = cap.shape[:2]
center = (w//2, h//2)
rotation_matrix = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated_video = cv2.warpAffine(cap, rotation_matrix, (w, h))
cv2.imshow('Rotated Video', rotated_video)

cropped_video = cap[50:300, 100:400]
cv2.imshow("Cropped Video", cropped_video)

bright = cv2.convertScaleAbs(cap, alpha=1.5, beta=50)
cv2.imshow("Brightened Video", bright)


if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()



