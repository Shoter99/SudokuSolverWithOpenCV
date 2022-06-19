import trainningDataPreprocessing as dataset
import numpy as np
import tensorflow as tf
#import tflite
import keras
import os
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D


global classes
classes = 9


filePath = "PrintedDigitRecognition13.h5"
liteFilePath = "PrintedDigitRecognition13.tflite"#os.path.join("PythonScrpts","PrintedDigitRecognition13.tflite") #"PrintedDigitRecognitionLite13.h5")
print(liteFilePath)


def make_model():
    trainImg, trainLab, testImg, testLab = dataset.get_processed_datasets(trainingSize=20000)
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
    model.compile(loss ='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    hist = model.fit(trainImg, trainLab, batch_size = 1000, epochs = 10) 


    model.save(filePath)
    score = model.evaluate(testImg,testLab, verbose = 0)
    print("score:", score)
    return model

def convert():
    model = keras.models.load_model("PrintedDigitRecognition13.h5")
    print("model:", type(model))

 
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tfLiteModel = converter.convert()
    with open(liteFilePath, "wb") as wfile:
        wfile.write(tfLiteModel)


make_model()

convert()
