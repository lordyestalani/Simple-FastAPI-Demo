from fastapi import FastAPI # Imports Fast API
from pydantic import BaseModel # Imports Base Model

app = FastAPI() # Creates the App Object

todo_db = {} # Creates an empty python dictionary
next_task_id = 1 # Task ID Counter

class TaskCreate(BaseModel): # Defines a Pydantic Model for the data someone sends to create a task
    title: str # What a piece of data should contain

@app.get("/tasks") # Tells FastAPI to call this function when it receives a GET request at /tasks
def list_tasks(): # Defines the function 
    return list(todo_db.values()) # Return list

@app.post("/tasks") # Tells FastAPI to call this function when it receives a POST request at /tasks
async def create_task(task: TaskCreate): # Checks against the "rules" > title: str as defined in TaskCreate Class
    global next_task_id # Update the Task ID Counter

    new_task = {"id": next_task_id, "title": task.title, "done": False} # Builds the task with its ID, "done" set to False as default
    todo_db[next_task_id] = new_task # Saves it under that ID
    next_task_id += 1 # Increments counter for the next request
        
    return new_task # Return Task

@app.get("/tasks/{task_id}") # {task_id} is a placeholder in the URL. If you open /tasks/1, FastAPI passes 1 to the function
def get_task(task_id: int): # Read {task_id} as int (Whole Number)
    return todo_db.get(task_id) # Return Task with specified ID