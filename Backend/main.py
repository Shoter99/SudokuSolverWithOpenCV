from fastapi import FastAPI
from pydantic import BaseModel
from PythonScripts.Sudoku import SolveSudoku
import json
app = FastAPI()

class Board(BaseModel):
    board: list

@app.post("/api/solve")
def home(board: Board):
    
    # print(SolveSudoku(res["board"]))
    return SolveSudoku(board.board)
@app.get('/api/test')
def test():
    return 'test'

# [[" ", "2", " ", "4", " ", "6", " ", " ", " "], [" ", " ", " ", " ", " ", "5", " ", "7", " "], [" ", " ", " ", "1", " ", " ", " ", "3", " "], [" ", "1", " ", "8", " ", "2", " ", "9", " "], [" ", " ", "2", " ", "5", " ", " ", " ", " "], [" ", " ", " ", " ", " ", "7", "8", " ", " "], [" ", " ", " ", "5", " ", "8", "9", " ", " "], ["4", " ", " ", " ", " ", "6", " ", " ", " "], [" ", " ", "1", "4", " ", " ", " ", " ", " "]]