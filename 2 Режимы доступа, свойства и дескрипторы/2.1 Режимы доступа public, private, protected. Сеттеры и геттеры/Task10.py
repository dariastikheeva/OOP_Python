from random import choice, randint
from string import ascii_letters, digits
class EmailValidator:
    CHARS = ascii_letters + digits + '_'
    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def get_random_email(cls):
        email = [choice(cls.CHARS) for _ in range(randint(1, 100))]
        return ''.join(email) + '@gmail.com'
    
    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        c1 = all(i in cls.CHARS + '@.' for i in email) and email.count('@') == 1
        before, after, *args = email.split('@')
        c2 = len(before) < 101 and len(after) < 51
        c3 = '.' in after
        c4 = '..' not in email
        return c1 and c2 and c3 and c4

    @staticmethod
    def __is_email_str(email):
        return type(email) is str
