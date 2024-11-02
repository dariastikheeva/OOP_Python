class InputDigits:
    def __init__(self, func):
        self.__fn = func
 
    def __call__(self, *args, **kwargs):
        return [int(i) for i in args[0]]
    
@InputDigits
def input_dg(s):
    return s

res = input_dg(input())
