import cv2

#import numpy as np


face_cascade = cv2.CascadeClassifier('G:/My Drive/FYP/Python Stuff/data/haarcascades/haarcascade_frontalface_alt2.xml')
captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture(0)
ret,frame = captureDevice.read()
cv2.imshow('frame',frame)

captureDevice.release()  
cv2.destroyAllWindows()




