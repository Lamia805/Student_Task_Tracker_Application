from datetime import datetime
import random

class Task:
    
    def __init__(self, title, description, status="Pending"):
        self.id=random.randint(1,1000)
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }
