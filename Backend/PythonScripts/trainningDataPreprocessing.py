
import glob
import cv2 as cv
import numpy as np
import os
import random

#dataset sources:
# http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/
# https://github.com/dharm1k987/sudoku-solver-opencv/tree/master/original

def format_image(picture):

    gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
    resized = cv.resize(gray, (32,32))
    blurred = cv.blur(resized, (3,3))
    adaptiveThresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 7, 5)
    return adaptiveThresh

def load_images():
    images = np.zeros((1,32,32))
    labels = np.zeros((1))

    for digitFolder in glob.glob("dataset//*"):
        currentDigit = int(digitFolder[-1]) -1
        batchOfImages = np.zeros((1,32,32))

        for imageAdress in glob.glob(digitFolder + "//*"):
            img = cv.imread(imageAdress)
            formatedImage = format_image(img)
            labels = np.append(labels, currentDigit)
            batchOfImages = np.concatenate((batchOfImages, [formatedImage]))
        
        batchOfImages = np.delete(batchOfImages, 0, 0)
        images = np.concatenate((images, batchOfImages))

    images = np.delete(images, 0, 0)
    labels = np.delete(labels, 0, 0)

    return (images,labels)

def randomize(images, labels):
    toRandomize = []
    for i,imagea in enumerate(images):
        toRandomize.append((imagea, labels[i]))

    random.shuffle(toRandomize)
    
    randImages = np.zeros((1,32,32))
    randLabels = np.zeros((1))

    i = 1000
    tmp = np.zeros((1,32,32))
    for pair in toRandomize:
        if i == 0:
            tmp = np.delete(tmp, 0, 0)
            randImages = np.concatenate((randImages, tmp))
            tmp = np.zeros((1,32,32))
            i = 1000
        
        tmp = np.concatenate((tmp, [pair[0]]))
        randLabels = np.append(randLabels, pair[1])
        i -= 1
    tmp = np.delete(tmp, 0, 0)
    randImages = np.concatenate((randImages, tmp))
    
    randImages = np.delete(randImages, 0, 0)
    randLabels = np.delete(randLabels, 0, 0)

    return randImages, randLabels

def get_processed_datasets(trainingSize = 8000):
    img, lab = load_images()
    img, lab = randomize(img,lab)
    
    trainImg = img[:trainingSize]/255
    trainImg = trainImg.astype('float32')
    trainLab = lab[:trainingSize] 
    testImg = img[trainingSize:]/255
    testImg = testImg.astype('float32')
    testLab = lab[trainingSize:]
    

    return trainImg, trainLab, testImg, testLab
