from .models import Task


def get_importance(tasks: Task) -> tuple[list, list, list]:
    h = []
    m = []
    l = []
    
    for task in tasks.order_by('-due_date'):
        if task.importance == 'H':
            h.append(task)
        elif task.importance == 'M':
            m.append(task)
        elif task.importance == 'L':
            l.append(task)

    return h, m, l