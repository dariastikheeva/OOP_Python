from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return 'Базовый класс Model'
    

class ModelForm(Model):
    __count = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        ModelForm.__count += 1
        self._id = ModelForm.__count

    def get_pk(self):
        return self._id
    