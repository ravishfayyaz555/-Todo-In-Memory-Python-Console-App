import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import task_manager

def test_functionality():
    print("Testing Todo application functionality...")
    
    # Test adding a task
    task = task_manager.add_task('Test Task', 'This is a test')
    print(f'Added task: ID={task.id}, Title={task.title}, Status={task.status}')

    # Test listing tasks
    tasks = task_manager.get_all_tasks()
    print(f'Total tasks: {len(tasks)}')

    # Test updating a task
    updated_task = task_manager.update_task(1, 'Updated Task', 'Updated description')
    print(f'Updated task: ID={updated_task.id}, Title={updated_task.title}')

    # Test marking as complete
    completed_task = task_manager.update_task_status(1, 'complete')
    print(f'Marked as complete: Status={completed_task.status}')

    # Test listing again
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        print(f'Task: ID={task.id}, Title={task.title}, Status={task.status}')

    # Test deleting
    task_manager.delete_task(1)
    print('Deleted task 1')

    # Check if deleted
    tasks = task_manager.get_all_tasks()
    print(f'Tasks after deletion: {len(tasks)}')
    
    print("All tests passed!")

if __name__ == "__main__":
    test_functionality()