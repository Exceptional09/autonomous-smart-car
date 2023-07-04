import cv2
import numpy as np
from keras.models import load_model





######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

model=load_model("model.h5")

cap = cv2.VideoCapture(1)
while True:

    ret, img = cap.read()
    cv2.imshow('IMG',img)
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    if steering >0.4:
        print("left")
    elif steering <-0.4:
        print("right")
    elif steering < 0.4 and steering >-0.4:
        print("straight")
    elif steering > 0.4 and steering <-0.4:
        print("stop")  
 
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()