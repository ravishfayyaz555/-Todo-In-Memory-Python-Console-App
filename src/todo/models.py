# src/models.py
from dataclasses import dataclass

@dataclass
class Task:
    """ Represents a single task in the to-do list. """
    id: int
    title: str
    description: str
    status: str  # "incomplete" or "complete"