from random import randint, choices

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
        self.__rpswd = ''

    def __call__(self, *args, **kwargs):
        self.__rpswd = choices(self.psw_chars, k=randint(self.min_length, self.max_length))
        return ''.join(self.__rpswd)
    
r = RandomPassword(psw_chars='qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*', min_length=5, max_length=20)
lst_pass = [r() for _ in range(3)]
