class ToDoList:
  def __init__(self):
      self.tasks = []

  def show_tasks(self):
      if not self.tasks:
          print("Your to-do list is empty.")
      else:
          print("To-Do List:")
          for i, task in enumerate(self.tasks, 1):
              status = "Done" if task["done"] else "Not Done"
              print(f"{i}. {task['description']} (Due: {task['due_date']}) - {status}")

  def add_task(self):
      description = input("Enter task description: ")
      due_date = input("Enter due date (optional): ")
      self.tasks.append({"description": description, "due_date": due_date, "done": False})
      print("Task added!")

  def mark_done(self):
      self.show_tasks()
      task_index = int(input("Enter the task number you want to mark as done: ")) - 1
      if 0 <= task_index < len(self.tasks):
          self.tasks[task_index]["done"] = True
          print("Task marked as done!")
      else:
          print("Invalid task number.")

  def update_task(self):
      self.show_tasks()
      task_index = int(input("Enter the task number you want to update: ")) - 1
      if 0 <= task_index < len(self.tasks):
          new_description = input("Enter new task description: ")
          new_due_date = input("Enter new due date (optional): ")
          self.tasks[task_index]["description"] = new_description
          self.tasks[task_index]["due_date"] = new_due_date
          print("Task updated!")
      else:
          print("Invalid task number.")

  def delete_task(self):
      self.show_tasks()
      task_index = int(input("Enter the task number you want to delete: ")) - 1
      if 0 <= task_index < len(self.tasks):
          deleted_task = self.tasks.pop(task_index)
          print(f"Task '{deleted_task['description']}' has been deleted.")
      else:
          print("Invalid task number.")

  def run(self):
      while True:
          print("\nOptions:")
          print("1. Show tasks")
          print("2. Add a task")
          print("3. Mark a task as done")
          print("4. Update a task")
          print("5. Delete a task")
          print("6. Quit")

          choice = input("Enter your choice: ")

          if choice == "1":
              self.show_tasks()
          elif choice == "2":
              self.add_task()
          elif choice == "3":
              self.mark_done()
          elif choice == "4":
              self.update_task()
          elif choice == "5":
              self.delete_task()
          elif choice == "6":
              break
          else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
  todo_list = ToDoList()
  todo_list.run()
