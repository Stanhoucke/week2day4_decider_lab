from src.task import Task

# def get_preferred_option(task_1, task_2):
#     if task_1.name == "Wash Dishes" or task_1.name == "Cook Dinner" or task_1.name == "Clean Windows":    
#         return task_1
    # elif task_2.name == "Cook Dinner":
    #     return task_2

def get_preferred_option(task_1, task_2):
    if task_1.name == "Wash Dishes" and task_2.name == "Cook Dinner":
        return task_1
    elif task_1.name == "Cook Dinner" and task_2.name == "Wash Dishes":
        return task_2
    elif task_1.name == "Cook Dinner" and task_2.name == "Clean Windows":
        return task_1
    elif task_1.name == "Clean Windows" and task_2.name == "Cook Dinner":
        return task_2
    elif task_1.name == "Clean Windows" and task_2.name == "Wash Dishes":
        return task_1
    elif task_1.name == "Wash Dishes" and task_2.name == "Clean Windows":
        return task_2
    else:
        return "Undefined task"

    # [task_1, task_2]

    # ["Wash Dishes", "Cook Dinner"]

    # ["Cook Dinner", "Clean Windows"]

    # ["Clean Windows", "Wash Dishes"]