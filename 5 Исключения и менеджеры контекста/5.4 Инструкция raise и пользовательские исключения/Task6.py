# здесь объявляйте классы
from datetime import datetime


class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        try:
            self.date_string = datetime.strptime(date_string, "%d.%m.%Y").strftime(
                "%d.%m.%Y"
            )
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date_string


date_string = input()

# здесь создавайте объект класса DateString и выполняйте обработку исключений
try:
    date = DateString(date_string)
except DateError:
    print("Неверный формат даты")
else:
    print(date)
    