import copy
import random

sudoku = [[], [], [], [], [], [], [], [], []]

def SolveSudoku(sudoku):

    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    repeat = True
    numbersLeft = 81
    pierwszyRaz = True
            
    for i in range (9):
        for j in range (9):
            if sudoku[i][j] != ' ':
                numbersLeft -= 1

           
    while numbersLeft!=0:
        while repeat:       
            repeat = False
            avaiblePlaces = {}
            avaibleNumbers = {}
            for i in range (9):
                for j in range(9):
                    avaiblePlaces[str(i)+str(j)] = 0
                    avaibleNumbers[str(i)+str(j)] = 0
                            
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
                            repeat = True
                            sudoku[placei][placej] = number
                            numbersLeft -= 1
            
            try:
                
                for z in range(0, 9, 3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 3+z):
                        for j in range (0, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 3+z):
                            for j in range (0, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True

                    numberToAdd = list(numbers)        
                    for i in range (0+z, 3+z):
                        for j in range (3, 6):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 3+z):
                            for j in range (3, 6):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True


                    numberToAdd = list(numbers)
                    for i in range (0+z, 3+z):
                        for j in range (6, 9):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 3+z):
                            for j in range (6, 9):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True
                                    


                for z in range(3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 9, 3):
                        for j in range (0, 9, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 9, 3):
                            for j in range (0, 9, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True


                    numberToAdd = list(numbers)        
                    for i in range (0+z, 9, 3):
                        for j in range (1, 9, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 9, 3):
                            for j in range (1, 9, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True


                    numberToAdd = list(numbers)
                    for i in range (0+z, 9, 3):
                        for j in range (2, 9, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 9, 3):
                            for j in range (2, 9, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    repeat = True


            except:
                
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
                repeat = True
                continue
                
            if repeat == False:
                for i in range(9):
                    for j in range(9):
                         if avaiblePlaces[str(i)+str(j)] == 1:
                            sudoku[i][j] = avaibleNumbers[str(i)+str(j)]
                            numbersLeft -= 1
                            repeat = True

                if numbersLeft == 0:
                    return sudoku

                if repeat == False:
                    if pierwszyRaz:
                        savedNumbersLeft = numbersLeft
                        pierwszyRaz = False
                        testSudoku = []
                        testSudoku = copy.deepcopy(sudoku)
                    else:
                        q = 1
                        if int(q) == 2:
                            sudoku = []
                            sudoku = copy.deepcopy(testSudoku)
                            numbersLeft = savedNumbersLeft
                    
                    while True:
                        
                        i = random.randint(0, 8)
                        j = random.randint(0, 8)                   
                        if sudoku[int(i)][int(j)] == ' ':
                            number = random.randint(1, 9)
                            break
                        
                    sudoku[int(i)][int(j)] = str(number)
                    numbersLeft -= 1
                    repeat = True            

    return sudoku
