import tensorflow as tf
import keras
import cv2 as cv
import PythonScripts.trainningDataPreprocessing
import numpy as np


model = keras.models.load_model("PrintedDigitRecognition13.h5")

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

