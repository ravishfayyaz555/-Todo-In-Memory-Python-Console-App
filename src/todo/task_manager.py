# src/task_manager.py
from typing import List, Optional
from .models import Task

# --- In-Memory Storage ---
_tasks: List[Task] = []
_next_id: int = 1

# --- Custom Exception ---
class TaskNotFoundError(Exception):
    """Custom exception raised when a task is not found."""
    pass

# --- Business Logic / Services ---
def add_task(title: str, description: str) -> Task:
    """
    Creates a new task, adds it to the in-memory list, and returns it.
    """
    global _next_id
    new_task = Task(
        id=_next_id,
        title=title,
        description=description,
        status="incomplete"
    )
    _tasks.append(new_task)
    _next_id += 1
    return new_task

def get_all_tasks() -> List[Task]:
    """
    Returns a list of all current tasks.
    """
    return _tasks

def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Finds and returns a task by its ID.
    Returns None if the task is not found.
    """
    for task in _tasks:
        if task.id == task_id:
            return task
    return None

def update_task(task_id: int, title: Optional[str], description: Optional[str]) -> Task:
    """
    Updates a task's title and/or description.
    Raises TaskNotFoundError if the task ID does not exist.
    """
    task = get_task_by_id(task_id)
    if not task:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    return task

def update_task_status(task_id: int, status: str) -> Task:
    """
    Updates a task's status.
    Raises TaskNotFoundError if the task ID does not exist.
    """
    if status not in ["complete", "incomplete"]:
        raise ValueError("Status must be 'complete' or 'incomplete'.")
    task = get_task_by_id(task_id)
    if not task:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
    task.status = status
    return task

def delete_task(task_id: int) -> bool:
    """
    Deletes a task by its ID.
    Returns True if deletion was successful, raises TaskNotFoundError otherwise.
    """
    task = get_task_by_id(task_id)
    if not task:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
    _tasks.remove(task)
    return True