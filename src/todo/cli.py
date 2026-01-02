# src/cli.py
import argparse
import sys
from . import task_manager
from .task_manager import TaskNotFoundError


def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(
        description="A simple CLI Todo application."
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # --- Add command ---
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument(
        "--title", type=str, required=True, help="The title of the task"
    )
    parser_add.add_argument(
        "--description", type=str, default="", help="The description of the task"
    )

    # --- List command ---
    subparsers.add_parser("list", help="List all tasks")

    # --- Update command ---
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="The ID of the task to update")
    parser_update.add_argument("--title", type=str, help="The new title of the task")
    parser_update.add_argument(
        "--description", type=str, help="The new description of the task"
    )

    # --- Delete command ---
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="The ID of the task to delete")

    # --- Complete command ---
    parser_complete = subparsers.add_parser(
        "complete", help="Mark a task as complete"
    )
    parser_complete.add_argument("id", type=int, help="The ID of the task to complete")

    # --- Incomplete command ---
    parser_incomplete = subparsers.add_parser(
        "incomplete", help="Mark a task as incomplete"
    )
    parser_incomplete.add_argument(
        "id", type=int, help="The ID of the task to mark as incomplete"
    )

    args = parser.parse_args()

    try:
        if args.command == "add":
            task = task_manager.add_task(args.title, args.description)
            print(f"Successfully added task {task.id}: '{task.title}'")

        elif args.command == "list":
            tasks = task_manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(
                        f"ID: {task.id}\n"
                        f" Title: {task.title}\n"
                        f" Description: {task.description}\n"
                        f" Status: {task.status}\n"
                        f"--------------------"
                    )

        elif args.command == "update":
            if args.title is None and args.description is None:
                print(
                    "Error: You must provide either --title or --description to update.",
                    file=sys.stderr,
                )
                sys.exit(1)
            task = task_manager.update_task(args.id, args.title, args.description)
            print(f"Successfully updated task {task.id}.")

        elif args.command == "delete":
            task_manager.delete_task(args.id)
            print(f"Successfully deleted task {args.id}.")

        elif args.command == "complete":
            task = task_manager.update_task_status(args.id, "complete")
            print(f"Task {args.id} marked as complete.")

        elif args.command == "incomplete":
            task = task_manager.update_task_status(args.id, "incomplete")
            print(f"Task {args.id} marked as incomplete.")

    except TaskNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()