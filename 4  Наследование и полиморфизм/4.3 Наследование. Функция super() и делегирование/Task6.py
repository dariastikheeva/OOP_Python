class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

# здесь объявляйте декоратор Callback
class Callback(object):
    def __init__(self, path, cls_route):
        self.path = path
        self.cls_route = cls_route

    def __call__(self, func):
        self.cls_route.add_callback(self.path, func)
        