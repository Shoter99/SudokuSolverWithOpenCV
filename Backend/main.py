from fastapi import FastAPI
from PythonScripts.test import test
app = FastAPI()


@app.get('/')
def home():
    return test()
