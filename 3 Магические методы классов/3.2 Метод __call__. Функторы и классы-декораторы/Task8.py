class Handler:
    def __init__(self, methods):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            r = request.get('method', 'GET')
            if r in self.__methods:
                if r == 'GET':
                    return self.get(func, request)
                else:
                    return self.post(func, request)
            else:
                return None
        return wrapper
    
    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
    
    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'
    