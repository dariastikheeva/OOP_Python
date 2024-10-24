class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
    
class PhoneBook:
    def __init__(self):
        self.numbers = []

    def add_phone(self, phone):
        self.numbers.append(phone)

    def remove_phone(self, indx):
        self.numbers.pop(indx)

    def get_phone_list(self):
        return self.numbers
