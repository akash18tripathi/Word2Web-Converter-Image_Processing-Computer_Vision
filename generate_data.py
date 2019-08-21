import numpy as np
import cv2 as cv

#Drawing on a stable image
drawing = False 
mode = False 
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(blackboard,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(blackboard,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(blackboard,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(blackboard,(x,y),5,(0,0,255),-1)


#Generating Data for head
for i in range(0,80):
    blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle)
    while(1):
        cv.imshow('image',blackboard)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()
       #Morphological transformations 
    lower_red = np.array([0,70,50])
    upper_red = np.array([10, 255, 255])
    hsv = cv.cvtColor(blackboard, cv.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.inRange(hsv, lower_red, upper_red) 
    mask = cv.resize(mask, (100,50))
    cv.imwrite("head"+str(i)+".jpg",mask)


#Generating Data
for i in range(0,80):
    blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle)
    while(1):
        cv.imshow('image',blackboard)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()
       #Morphological transformations 
    lower_red = np.array([0,70,50])
    upper_red = np.array([10, 255, 255])
    hsv = cv.cvtColor(blackboard, cv.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.inRange(hsv, lower_red, upper_red) 
    mask = cv.resize(mask, (100,50))
    cv.imwrite("nav"+str(i)+".jpg",mask)


#Generating Data
for i in range(0,80):
    blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle)
    while(1):
        cv.imshow('image',blackboard)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()
       #Morphological transformations 
    lower_red = np.array([0,70,50])
    upper_red = np.array([10, 255, 255])
    hsv = cv.cvtColor(blackboard, cv.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.inRange(hsv, lower_red, upper_red) 
    mask = cv.resize(mask, (100,50))
    cv.imwrite("main"+str(i)+".jpg",mask)
