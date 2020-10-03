from fastapi import FastAPI, Response

app = FastAPI()

tasks = {"foo": "Listen to the Bar Fighters"}

@app.put('/get-or-create/{task_id}', status_code=200)
async def get_or_create(task_id: str, res: Response):
    if task_id not in tasks:
        tasks[task_id] = "This didn't exist before"
        res.status_code = 201
    return tasks[task_id]
