from src.task import Task

def get_preferred_option(task_1, task_2):
    if task_1.name == "Wash Dishes" or task_1.name == "Cook Dinner":    
        return task_1
    # elif task_2.name == "Cook Dinner":
    #     return task_2