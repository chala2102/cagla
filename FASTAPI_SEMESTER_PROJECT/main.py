from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from helpers import load_tasks, save_tasks, generate_id, current_timestamp

# FastAPI uygulaması
app = FastAPI(title="Task Manager API")

# Task veri modeli
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: str = "medium"
    created_at: str
    updated_at: Optional[str] = None
    notes: Optional[str] = None

# Task oluşturma modeli (ID otomatik)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    notes: Optional[str] = None

# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI Task Manager is running"}

# Tüm taskları veya filtrelenmiş taskları getir
@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None, priority: Optional[str] = None):
    tasks = load_tasks()
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    if priority is not None:
        tasks = [t for t in tasks if t["priority"] == priority]
    return tasks

# Tek task getir
@app.get("/tasks/{id}")
def get_task(id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Task oluştur
@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks = load_tasks()
    new_id = generate_id(tasks)
    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": False,
        "priority": task.priority,
        "created_at": current_timestamp(),
        "updated_at": None,
        "notes": task.notes
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return {"message": "Task added successfully", "task": new_task}

# Task güncelle
@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):
    tasks = load_tasks()
    for idx, task in enumerate(tasks):
        if task["id"] == id:
            updated_dict = updated_task.dict()
            updated_dict["updated_at"] = current_timestamp()
            tasks[idx] = updated_dict
            save_tasks(tasks)
            return {"message": "Task updated successfully", "task": updated_dict}
    raise HTTPException(status_code=404, detail="Task not found")

# Tek task sil
@app.delete("/tasks/{id}")
def delete_task(id: int):
    tasks = load_tasks()
    filtered = [t for t in tasks if t["id"] != id]
    if len(filtered) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    save_tasks(filtered)
    return {"message": "Task deleted successfully"}

# Tüm taskları sil
@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks cleared"}

# Tasklarda arama
@app.get("/tasks/search")
def search_tasks(query: str = Query(..., min_length=1)):
    tasks = load_tasks()
    results = [
        t for t in tasks
        if query.lower() in t["title"].lower() or (t["description"] and query.lower() in t["description"].lower())
    ]
    return results

# Task istatistikleri
@app.get("/tasks/stats")
def task_stats():
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(t["completed"] for t in tasks)
    pending = total - completed
    percent_complete = (completed / total * 100) if total else 0
    priorities = {"low": 0, "medium": 0, "high": 0}
    for t in tasks:
        priorities[t["priority"]] += 1
    most_common_priority = max(priorities, key=priorities.get) if total else None
    return {
        "total_tasks": total,
        "completed": completed,
        "pending": pending,
        "percent_complete": round(percent_complete, 2),
        "priorities": priorities,
        "most_common_priority": most_common_priority
    }

# Opsiyonel: Tüm endpoint URL’lerini terminalde listele
if __name__ == "__main__":
    for route in app.routes:
        print(f"Path: {route.path}, Methods: {route.methods}")