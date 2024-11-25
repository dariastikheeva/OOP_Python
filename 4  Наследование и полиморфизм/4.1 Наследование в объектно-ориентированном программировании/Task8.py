class Validator:
    def _is_valid(self, data):
        return True
    
    def __call__(self, data):
        if self._is_valid(data):
            return data
        else:
            raise ValueError('данные не прошли валидацию')
        
class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value
