import copy
import random

def SolveSudoku(sudoku):

    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    numbersLeft = 81
    firstTime = True
            
    for i in range (9):
        for j in range (9):
            if sudoku[i][j] != ' ':
                numbersLeft -= 1
     
    for attempt in range(5000):
        
        numberWasAdded = False
        avaiblePlaces = {}
        avaibleNumbers = {}
        
        for i in range (9):
            for j in range(9):
                avaiblePlaces[str(i)+str(j)] = 0

        try:
            
            for z in range(0, 9, 3):
                for k in range (0, 9, 3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 3+z):
                        for j in range (0+k, 3+k):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 3+z):
                            for j in range (0+k, 3+k):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    numberWasAdded = True
                                
            for z in range(3):
                for k in range (3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 9, 3):
                        for j in range (0+k, 9, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 9, 3):
                            for j in range (0+k, 9, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    numberWasAdded = True

        except ValueError:

            try:
            
                numbersLeft = savedNumbersLeft
                sudoku = copy.deepcopy(testSudoku)
                while True:
                        i = random.randint(0, 8)
                        j = random.randint(0, 8)
                        if sudoku[int(i)][int(j)] == ' ':
                            number = random.randint(1, 9)
                            break
                sudoku[int(i)][int(j)] = str(number)
                numbersLeft -= 1
                numberWasAdded = True
                continue
        
            except UnboundLocalError:
                
                return 'Cannot solve'
                        
        for number in numbers:
            for i in range (9):
                if sudoku[i].count(number) == 0:
                    places = 0
                    placei = 0
                    placej = 0
                    for j in range (9):
                        if sudoku[i][j] == ' ':
                            works = True
                            
                            for i1 in range (groups[i//3][0], groups[i//3][2]+1):
                                for j1 in range(groups[j//3][0], groups[j//3][2]+1):
                                    if sudoku[i1][j1] == number:
                                        works = False

                            for i2 in range (i%3, 9, 3):
                                for j2 in range(j%3, 9, 3):
                                    if sudoku[i2][j2] == number:
                                        works = False
                            if works:
                                avaiblePlaces[str(i)+str(j)] += 1
                                avaibleNumbers[str(i)+str(j)] = number
                                places += 1
                                placei = i
                                placej = j

                    if places == 1:
                        numberWasAdded = True
                        sudoku[placei][placej] = number
                        numbersLeft -= 1

        for i in range(9):
            for j in range(9):
                if avaiblePlaces[str(i)+str(j)] == 1 and sudoku[i][j] == ' ':
                    sudoku[i][j] = avaibleNumbers[str(i)+str(j)]
                    numbersLeft -= 1
                    numberWasAdded = True
         
        if numberWasAdded == False:

            if numbersLeft == 0:
                return sudoku

            if numberWasAdded == False:
                if firstTime:
                    savedNumbersLeft = numbersLeft
                    firstTime = False
                    testSudoku = []
                    testSudoku = copy.deepcopy(sudoku)
                
                while True:
                    
                    i = random.randint(0, 8)
                    j = random.randint(0, 8)                   
                    if sudoku[int(i)][int(j)] == ' ':
                        number = random.randint(1, 9)
                        break
                    
                sudoku[int(i)][int(j)] = str(number)
                numbersLeft -= 1
                numberWasAdded = True
                
    return 'Cannot solve'
