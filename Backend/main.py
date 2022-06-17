import os
from fastapi import FastAPI, File, UploadFile
from random import randint
from pydantic import BaseModel
from PythonScripts.Sudoku import SolveSudoku
from PythonScripts.photoToArray import photo_to_array
import json
app = FastAPI()

class Board(BaseModel):
    board: list

@app.post("/api/solve")
def sovle(board: Board):
    # print(SolveSudoku(res["board"]))
    print("Request recieved!")
    res = SolveSudoku(board.board)
    print(res)
    if not res:
        return {'error': 'Something went wrong! Try again'}
    if res == "Cannot Solve":
        return {'error': 'Sorry Sudoku is not solvable, try different one'}
    return res
@app.get('/api/test')
def test():
    return 'test'

@app.post('/api/read_numbers')
def read_numbers(photo: bytes = File(...)):
    rand = randint(1,1000)
    filename = f'image{rand}.jpg'
    #filename = 'test.png'
    with open(filename, 'wb') as img:
        img.write(photo)
    outputArray = photo_to_array(filename)  
    os.remove(filename)    
    return outputArray



# [[" ", "2", " ", "4", " ", "6", " ", " ", " "], [" ", " ", " ", " ", " ", "5", " ", "7", " "], [" ", " ", " ", "1", " ", " ", " ", "3", " "], [" ", "1", " ", "8", " ", "2", " ", "9", " "], [" ", " ", "2", " ", "5", " ", " ", " ", " "], [" ", " ", " ", " ", " ", "7", "8", " ", " "], [" ", " ", " ", "5", " ", "8", "9", " ", " "], ["4", " ", " ", " ", " ", "6", " ", " ", " "], [" ", " ", "1", "4", " ", " ", " ", " ", " "]]
