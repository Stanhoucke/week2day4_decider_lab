class Task:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def task_preference(self, preferred_task):
        if preferred_task == "Wash Dishes":    
            return preferred_task