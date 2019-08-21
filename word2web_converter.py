from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template,Response
import numpy as np
import cv2 as cv
from keras.models import load_model


app = Flask(__name__)


d = {
     0: "HEAD",
     1:"NAV",
     2:"MAIN"
     
     }
drawing = False 
mode = False 
ix,iy = -1,-1

def gen():
    
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
                    
    
    
    blackboard = np.zeros((480, 640, 3), dtype=np.uint8)

    cv.namedWindow('image')
    cv.setMouseCallback('image',draw_circle)
    #Writing on blackboard
    while(1):
        cv.imshow('image',blackboard)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()
    
    model = load_model('model.h5')
    #Setting hsv value for red
    lower_red = np.array([0,70,50])
    upper_red = np.array([10, 255, 255])
    
    #Converting into hsv and then applying masking
    hsv = cv.cvtColor(blackboard, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_red, upper_red)
    
    mask = cv.resize(mask, (100,100))
    img = np.array(mask, dtype=np.float32)
    img = np.reshape(mask, (-1, 100, 100, 1))
    #Predicting the written word
    predict_probablity = model.predict(img)[0]
    pred = list(predict_probablity).index(max(predict_probablity))
    
    return str(d[pred])


@app.route("/")
def hello():
   
    s= gen()
    if s=="HEAD" :
        return render_template('head.html')
    elif s=="NAV":
        return render_template('navigation.html')
    elif s=="MAIN":
        return render_template('main.html')
    else:
        return "Word not recognised"

if __name__ =="__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
