from code import InteractiveInterpreter
import tflite
import keras
import cv2 as cv
import numpy as np


#Interpreter
#interpreter = tf.lite.Interpreter("PrintedDigitRecognition13.tflite")
model = keras.models.load_model()
print("model:", type(model))

def predictDigit(img):

    img = img/255
    mid = img[8:24,8:24]  
    img = img.reshape(1,32,32,1)

    avg = np.average(mid)

    if avg < 0.1:
        return 0
    
    results = model.predict(img)[0]
    digit = 0
    maxResult = 0
    for i in range(len(results)):
        if results[i]>maxResult:
            maxResult = results[i]
            digit = i
    return digit+1

