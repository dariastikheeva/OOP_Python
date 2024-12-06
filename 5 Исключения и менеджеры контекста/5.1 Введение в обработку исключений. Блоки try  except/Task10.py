class Validator:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

class FloatValidator(Validator):
    def __call__(self, value):
        if not isinstance(value, float) or self._min_value > value  or self._max_value < value:
            raise ValueError('значение не прошло валидацию')

class IntegerValidator(Validator):
    def __call__(self, value):
        if not isinstance(value, int) or self._min_value > value or self._max_value < value or type(value) is bool:
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    res_lst = []
    for val in lst:
        for validator in validators:
            try:
                validator(val)
                res_lst.append(val)
            except:
                pass
    return res_lst
