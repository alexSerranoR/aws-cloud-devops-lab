from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn AWS",
        "completed": False
    }
]

app = FastAPI(
    title="AWS Cloud DevOps Lab",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AWS Cloud DevOps Lab API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloud-devops-api",
        "version": "0.1.0"
    }

@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    if completed is None:
        return tasks

    return [
        task
        for task in tasks
        if task["completed"] == completed
    ]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

class TaskCreate(BaseModel):
    title: str

@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task_data.title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return {
                "message": "Task deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )