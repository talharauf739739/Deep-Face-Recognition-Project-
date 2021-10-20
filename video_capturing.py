
import cv2
#import numpy as np

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
i = 0
while(i<=10):
    i = i+1
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)  #for converting in grayscale
    
    faces = face_cascade.detectMultiScale(gray) #We will get x,y,w and height in face variable
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+h] #Region of interest
        roi_color = frame[y:y+h,x:x+h]
        if i == 1:
            img_item = "mypic1.jpg"   #Path where pic will be save
        if i == 2:
            img_item = "mypic2.jpg"   #Path where pic will be save
        if i == 3:
            img_item = "mypic3.jpg"   #Path where pic will be save
        if i == 4:
            img_item = "mypic4.jpg"   #Path where pic will be save
        if i == 5:
            img_item = "mypic5.jpg"   #Path where pic will be save
        if i == 6:
            img_item = "mypic6.jpg"   #Path where pic will be save
        if i == 7:
            img_item = "mypic7.jpg"   #Path where pic will be save
        if i == 8:
            img_item = "mypic8.jpg"   #Path where pic will be save
        if i == 9:
            img_item = "mypic9.jpg"   #Path where pic will be save
        if i == 10:
            img_item = "mypic10.jpg"   #Path where pic will be save
        dim = (225,225)
        Saved_picture = cv2.resize(roi_color,dim)
        
        cv2.imwrite(img_item, Saved_picture ) #writing captured image in jpg file 
        
        color = (255,0,0) #blue color
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame,(x,y) , (end_cord_x,end_cord_y) , color, stroke)
    cv2.imshow('frame',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break   
cap.release()  
cv2.destroyAllWindows()