import numpy as np
import cv2 as cv
from PythonScripts.FindingEdgesAndSlicing import slicePhoto
from PythonScripts.modelHandling import predictDigit
import sys


def photo_to_array(img_path):
    img = cv.imread(img_path)
    sliceList = slicePhoto(img)
    digitList = []
    for row in sliceList:
        digitRow = []
        for digitImg in row:
            digitRow.append(predictDigit(digitImg))
        digitList.append(digitRow)
    return digitList
