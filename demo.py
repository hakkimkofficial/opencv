# import cv2
# image=cv2.imread('lena.jpg',1)
#
#
# cv2.imshow('image',image)
# cv2.waitKey(10000)
#
import cv2

# Load an image
# img = cv2.imread("lena.jpg")

# # Check if the image loaded successfully
# if img is not None:
#     # Display the image
#     cv2.imshow("Test Image", img)
#     cv2.waitKey(10000)
#     cv2.imwrite('lena.png',img)
#     cv2.destroyAllWindows()
# else:
#     print("Failed to load image")


#---------- Draw shapes -------------------------
# image=cv2.imread('lena.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,0),5)
# cv2.rectangle(image,(0,0),(400,400),(0.255,0),3)
# cv2.circle(image,(200,200),100,(0,0,255),-1)
# font=cv2.FONT_HERSHEY_DUPLEX
# cv2.putText(image,'hello',(100,100),font,4,(255,255,255),cv2.LINE_AA)

# cv2.imshow('shapes',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#--------------------------------------------------

#---------Mouse event ------------------
# def draw_circle(event,x,y,flag,param):
#     if event ==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(image,(x,y),100,(255,0,0),-1)
# image=cv2.imread('lena.jpg',1)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)

# while(1):
#     cv2.imshow('image',image)
#     if cv2.waitKey(20) & 0xFF == 27 :
#         break
# cv2.destroyAllWindows()            
#----------------------------------------


# -------object tracking-------------
# import numpy as np
# image=cv2.imread('blue.png',1)
# cv2.imshow('orginal',image)
# new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# cv2.imshow('image',new_image)

# lower_bound=np.array([110,50,50])
# upper_bound=np.array([130,252,252])
# mask=cv2.inRange(new_image,lower_bound,upper_bound)
# cv2.imshow('mask',mask)
# res=cv2.bitwise_and(image,image,mask=mask)
# cv2.imshow('res',res)

# blue=np.uint8([[[255,0,0]]])
# hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
# print(hsv_blue)

# cv2.waitKey(0)
#------- video tracking-----------#
import numpy as np
# image=cv2.imread('blue.png',1)
# cv2.imshow('orginal',image)
cap=cv2.VideoCapture(0)
while(1):
        _,frame=cap.read()
        new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow('image',new_image)

        lower_bound=np.array([110,50,50])
        upper_bound=np.array([130,252,252])
        mask=cv2.inRange(new_image,lower_bound,upper_bound)
        cv2.imshow('mask',mask)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('res',res)

        k=cv2.waitKey(5) & 0xFF
        if k ==27:
          break
cv2.destroyAllWindows()        

