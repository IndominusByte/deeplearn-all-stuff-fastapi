"""
Using BackgroundTasks also works with the dependency injection system, you can declare a parameter of type BackgroundTasks at multiple levels: in a path operation function, in a dependency (dependable), in a sub-dependency, etc.

FastAPI knows what to do in each case and how to re-use the same object, so that all the background tasks are merged together and are run in the background afterwards:
"""
from fastapi import FastAPI, BackgroundTasks, Depends
from typing import Optional

app = FastAPI()

def write_log(message: str):
    with open("log_dependency.txt", mode="a") as log:
        log.write(message)

def get_query(background_task: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_task.add_task(write_log, message)
    return q

@app.post('/send-notif/{email}', status_code=202)
async def send_notif(email: str, background_task: BackgroundTasks, q: get_query = Depends()):
    message = f"message to {email}\n"
    background_task.add_task(write_log, message)
    return {"message": "Message sent"}
