import PythonScripts.trainningDataPreprocessing
import numpy as np
import tensorflow as tf
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import keras
import os
global classes
classes = 9

def make_model():
    trainImg, trainLab, testImg, testLab = trainningDataPreprocessing.get_processed_datasets(trainingSize=20000)
    trainLab = keras.utils.np_utils.to_categorical(trainLab, classes)
    testLab = keras.utils.np_utils.to_categorical(testLab, classes)

    model = keras.models.Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(32,32,1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(classes, activation='softmax'))
    model.compile(loss ='categorical_crossentropy', optimizer="adam"   , metrics=['accuracy'])
    hist = model.fit(trainImg, trainLab, batch_size = 1000, epochs = 10) 
    
    model.save(os.path.join("PythonScrpts","PrintedDigitRecognition13.h5"))

    score = model.evaluate(testImg,testLab, verbose = 0)
    print("score:", score)
    return model


make_model()