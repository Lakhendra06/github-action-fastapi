# I need a fast api code here in main.py file
# I need to create a fast api code that will take a json input and return a json output

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# I need a code for my main.py file that will have the following functions:
# 1. A function that will take a string as input and return the string reversed.

@app.get("/reverse/{item}")
def reverse_string(item: str):
    return item[::-1]
