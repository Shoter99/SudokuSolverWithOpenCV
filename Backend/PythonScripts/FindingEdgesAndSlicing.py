import cv2 as cv
import numpy as np

def sort_points(list):

    local = list.copy()
    local = np.array(local).reshape(4,2)
    f1,f2,f3,f4 = local
   
    sorted = [[0,0],[0,0],[0,0],[0,0]]
    maxI = 0
    while len(local) >0:
        for i in range(len(local)):
            if local[i][0]>sorted[len(list)-len(local)][0]:
                sorted[len(list)-len(local)] = local[i]
                maxI = i

        local = np.delete(local, maxI, 0)
        
    if sorted[0][1]>sorted[1][1]:
        sorted[1],sorted[0] = sorted[0],sorted[1]
    if sorted[2][1]<sorted[3][1]:
        sorted[2],sorted[3] = sorted[3],sorted[2]

    sorted[0], sorted[1], sorted[2], sorted[3] = sorted[3], sorted[0], sorted[1], sorted[2]
    sorted = np.array(sorted).reshape((4,1,2))
    return np.array(tuple(sorted))

def cornersPreprocessImg(img):

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred = cv.blur(gray, (5,5) )
    adaptiveThresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 7, 5)
    dilated = cv.dilate(adaptiveThresh,(11,11), iterations=4)
    eroded = cv.erode(dilated,(11,11), iterations=4)

    return eroded

def findCorners(img):
    contours, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    blank = np.zeros_like(img, dtype="uint8")
    largestSqr = None

    for cont in contours:

        perimeter = cv.arcLength(cont, closed=True)
        square = cv.approxPolyDP(cont, 0.01 * perimeter, closed=True)

        area = cv.contourArea(square)
        if len(square) == 4:
            if area > (img.shape[0]*img.shape[1])/4:
                if largestSqr is None:
                    largestSqr = square
                if cv.contourArea(largestSqr) < cv.contourArea(square):
                    largestSqr = square

    if largestSqr is None:
        print("board not found")
        cv.waitKey(0)
    board = sort_points(largestSqr)

    return board
        
def transformImg(img,sqrPoints):

    srcCords = np.reshape(sqrPoints,(4,2))
    srcCords = np.array(srcCords, np.float32)
    dstCords = np.array(([0.0,0.0], [360.0,0.0], [360.0,360.0], [0.0,360.0]), np.float32).reshape((4,2))
    
    matrix = cv.getPerspectiveTransform(srcCords, dstCords)
    wrappedImg = cv.warpPerspective(img, matrix, (360, 360))
    return wrappedImg

def sliceDigits(sqrBoard):
    digits = [ [] for i in range(9) ]
    
    for i in range(9):
        for j in range(9):
            dig = sqrBoard[i*40:(i+1)*40,j*40:(j+1)*40]
            digits[i].append(preprocessDigit(dig)) 
    return digits

def preprocessDigit(board):

    gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
    blurred = cv.blur(gray, (3,3))
    adaptiveThresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 7, 5)
    cutEdges = adaptiveThresh[4:36,4:36]

    return cutEdges

def slicePhoto(img):
    processed = cornersPreprocessImg(img)
    corners = findCorners(processed)
    board = transformImg(img, corners)
    sliced = sliceDigits(board)
    return sliced



