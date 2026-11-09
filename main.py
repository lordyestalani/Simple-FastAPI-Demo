from fastapi import FastAPI # Imports Fast API
from pydantic import BaseModel # Imports Base Model

app = FastAPI() # Creates the App Object

todo_db = {} # Creates an empty python dictionary

class TaskCreate(BaseModel): # Defines a Pydantic Model for the data someone sends to create a task
    title: str # What a piece of data should contain

@app.get("/tasks") # Tells FastAPI to call this function when it receives a GET request at /tasks
def list_tasks(): # Defines the function 
    return list(todo_db.values()) # Return list