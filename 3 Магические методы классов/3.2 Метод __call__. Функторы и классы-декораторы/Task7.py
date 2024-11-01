class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request):
        if request.get('method', 'GET') == 'GET':
            return self.get(self.__fn, request)
        else:
            return None
        
    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
