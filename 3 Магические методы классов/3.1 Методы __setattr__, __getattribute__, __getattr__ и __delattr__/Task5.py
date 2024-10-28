class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('practices', 'duration') and not (isinstance(value, int) and value > 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
    
    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        object.__delattr__(self, item)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)
