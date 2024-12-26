class Test:
    def __init__(self, descr):
        self.descr = descr

    def __setattr__(self, name, value):
        if name == 'descr' and (len(value) < 10 or len(value) > 10000):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        return super().__setattr__(name, value)
    
    def run(self):
        raise NotImplementedError
    

class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, name, value):
        if name in ('ans_digit', 'max_error_digit'):
            if type(value) not in (int, float) or (name == 'max_error_digit' and value < 0):
                raise ValueError('недопустимые значения аргументов теста')
        return super().__setattr__(name, value)
    
    def run(self):
        ans = float(input())
        min_bound = self.ans_digit - self.max_error_digit
        max_bound = self.ans_digit + self.max_error_digit
        return ans >= min_bound and ans <= max_bound
    

descr, ans = map(str.strip, input().split('|'))
ans = float(ans)

try:
    t = TestAnsDigit(descr, ans)
except Exception as e:
    print(e)
else:
    try:
        print(t.run())
    except Exception as e:
        print(e)
