from fastapi import FastAPI # Imports Fast API

app = FastAPI() # Creates the App Object

todo_db = {} # Creates an empty python dictionary

@app.get("/tasks") # Tells FastAPI to call this function when it receives a GET request at /tasks
def list_tasks(): # Defines the function 
    return list(todo_db.values()) # Return list