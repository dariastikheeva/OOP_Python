class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func().split()]
        return wrapper
    
class RenderDigit:
    def __call__(self, s):
        try:
            return int(s)
        except ValueError:
            return None
        
@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)
