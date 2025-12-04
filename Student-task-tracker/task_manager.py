from task import Task
import json
from datetime import datetime

class TaskManager:
    def __init__(self,file_name="task.json"):
     self.file_name=file_name
     self.tasks=[]
     self.load_from_file()
    
    def add_task(self,title,description):
       task=Task(title,description)
       self.tasks.append(task)
       print("Task added successfully!!")

    def view_tasks(self):
     if not self.tasks:
        print("No tasks found ")
        return
     i=1
     for task in self.tasks:
        print("Task",i)
        print("ID :",task.id)
        print("Title :",task.title)
        print("Description :",task.description)
        print("status :",task.status)
        print("create_at :" ,task.created_at)
        i+=1
  
    def update_task(self,index,new_title="",new_description="",new_status=""):
       try:
          task=self.tasks[index]
          print(f"Title : {task.title}")
          new_title=input("Update Title : ")
          if new_title.strip():
             task.title=new_title
          print(f"Description : {task.description}")
          new_description=input("Update Description : ")
          if new_description.strip():
             task.description=new_description
          print(f"Status : {task.status}")
          
          new_status=input("Status (Pending/In Progress/Completed) : ")
          
          if new_status.strip():
           if new_status in ["Pending","In Progress","Completed"]:
             task.status=new_status
          task.created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          print("Task updated successfully")
         
       except IndexError:
          print("Invalid Task Index ")
    
    def delete_task(self,index):
     try:
       remove=self.tasks.pop(index)
       print(f"Task '{remove.title}' deleted successfully")
     except IndexError:
        print("Error: Invalid Task Index")
    
    def save_to_file(self):
       try:
          with open(self.file_name,"w") as f:
              json.dump([task.to_dict() for task in self.tasks],f,indent=4)
       except Exception as e:
          print("Error saving file:",e)
    
    def load_from_file(self):      
      try:
         with open(self.file_name, "r") as f:
           data=json.load(f)
           for d in data:
              task=Task(d["title"],d["description"],d["status"])
              task.id=d["id"]
              task.created_at=d["created_at"]
              self.tasks.append(task)

      except (FileNotFoundError,json.JSONDecodeError):
         self.tasks=[]
            
             
       
        
       
          
    
       

       
