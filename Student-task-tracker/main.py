from task_manager import TaskManager

def main():
    student=TaskManager()
    while True:
     print("===== Student Task Tracker ===== ")
     print("1.Add New Task")
     print("2.View All Tasks")
     print("3.Update Task")
     print("4.Delete Task")
     print("5.Exit")

     choice = input("Enter choice: ")
     if choice=="1":
           title=input("Task Title: ")
           description=input("Description: ")
           student.add_task(title,description)

     elif choice=="2":
           print("===>View All Tasks<===")
           student.view_tasks()

     elif choice=="3":
         print("===>Update Tasks<===")
         student.view_tasks()
         try:
              index=int(input("Enter the task number you want to update :")) -1
              
              student.update_task(index)
         except ValueError:
               print("Invalid Value, Please enter new value ")
      
     elif choice == "4":
        print("===>Delete Tasks<===")
        student.view_tasks()   
        try:
          index = int(input("Enter task number to delete: ")) - 1
          student.delete_task(index)
        except ValueError:
           print("Invalid input. Please enter a number.")

     elif choice=="5":
          student.save_to_file()
          print("Task saved.")
          print("Now Exit And Don't worry I track your task again ")
     else:
           print("Invalid choice, Please enter right choice")

if __name__ == "__main__":
      main()

       
           
         


