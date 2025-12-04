# Student_Task_Tracker_Application
<br>
1. Object-Oriented Programming (OOP) 

 Create a Task class to represent a single task: 

class Task: 

def init(self, title, description, created_at): 

self.title = title 

self.description = description 

self.created_at = created_at 

 Create a TaskManager class to handle all application operations, such as adding, viewing, updating, deleting tasks, and saving/loading from JSON. 

2. Functions (within Classes) 

Each action should be implemented as a method inside the classes, for example: 

 TaskManager.add_task() 

 TaskManager.view_tasks() 

 TaskManager.update_task() 

 TaskManager.delete_task() 

 TaskManager.save_to_file() 

 TaskManager.load_from_file() 

3. File Handling & JSON

 Tasks should be stored in a JSON file. 

 Load tasks from the JSON file when the program starts. 

 Save tasks to the JSON file when the program exits. 

4. Error Handling 

Use try-except blocks inside your class methods to handle:  File not found errors 

 Invalid input (e.g., index out of range) 

 JSON decoding errors 

5. Datetime Module 

 Each task should store the current date and time when created using datetime.now(). 

6. Modules 

 Use at least one built-in or external module. 

Example: Use the random module to generate a unique ID for each task. 

Sample User Flow 

===== Student Task Tracker ===== 

1. Add New Task 

2. View All Tasks 

3. Update Task 

4. Delete Task 

5. Exit 

Enter choice: 1 

Task Title: Study Python 

Description: Finish module 4 

Task added successfully! 

Expected JSON Structure (tasks.json) 

[

{  

"id": 123, 

"title": "Study Python", 

"description": "Finish module 4", 

"created_at": "2025-11-30 10:30:25" 

}
