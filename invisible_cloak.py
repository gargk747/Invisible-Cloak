import cv2
import numpy as np
import pickle

cap= cv2.VideoCapture(0)
back=cv2.imread('./demo.jpg')

while cap.isOpened():
    ret, frame= cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #how to get hsv value?
        #lower:hue-10,100,100   higher: hue+10,255,255
        red= np.uint8([[[50,50,150]]])#BGR  red
        hsv_red=cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #print(hsv_red)  #### this gives the HSV value of the corresponding BGR

        #setting the range of hsv value to get only red COLOR
        l_red= np.array([0,150,100])
        u_red= np.array([10,255,255])
        #defining kernel
        kernel = np.ones((2,2),np.uint8)
        #finding the red color in the image
        mask= cv2.inRange(hsv,l_red,u_red)
        #cv2.imshow("mask",mask)

        #removing that color from image
        part1= cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1",part1)

        #now inverse of that image
        mask=cv2.bitwise_not(mask)

        #removing inverse from that image
        part2= cv2.bitwise_and(frame, frame, mask=mask)
        #cv2.imshow("part2",part2)

        #now joining both the parts
        track=part1+part2

        #dilating the image for better performance
        dilation = cv2.dilate(track,kernel,iterations = 2)

        #show the MAGIC!!!!!!!!
        cv2.imshow("cloak",dilation)
        if cv2.waitKey(1)== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
