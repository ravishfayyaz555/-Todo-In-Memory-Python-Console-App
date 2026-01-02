"""Storage and business logic layer for the Todo application."""

from typing import List, Optional
from .models import Task


class TodoManager:
    """Manages todo tasks in memory with CRUD operations."""
    
    def __init__(self) -> None:
        """Initialize the todo manager with an empty task list."""
        self._tasks: List[Task] = []
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with the given title and optional description.
        
        Args:
            title: The task title (required)
            description: The task description (optional)
            
        Returns:
            The newly created Task object
            
        Raises:
            ValueError: If title is empty or whitespace-only
        """
        task = Task(id=self._next_id, title=title.strip(), description=description.strip())
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the system.
        
        Returns:
            List of all Task objects
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update a task's title or description.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            True if the task was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        
        # Re-validate the task after update
        if not task.title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only")
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self._tasks.remove(task)
        return True
    
    def toggle_task_status(self, task_id: int, completed: bool) -> bool:
        """Set the completion status of a task.
        
        Args:
            task_id: The ID of the task to update
            completed: The new completion status
            
        Returns:
            True if the task status was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = completed
        return True