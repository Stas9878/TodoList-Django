from django.db.models.query import QuerySet


def get_importance(tasks: QuerySet) -> tuple[list, list, list]:
    h = []
    m = []
    l = []
    
    for task in tasks:
        if task.importance == 'H':
            h.append(task)
        elif task.importance == 'M':
            m.append(task)
        elif task.importance == 'L':
            l.append(task)

    return h, m, l