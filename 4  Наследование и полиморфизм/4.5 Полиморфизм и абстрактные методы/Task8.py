from abc import ABC, abstractmethod

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name
        self.__population = population
        self.__square = square

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def population(self):
        return self.__population
    @population.setter
    def population(self, population):
        self.__population = population

    @property
    def square(self):
        return self.__square
    @square.setter
    def square(self, square):
        self.__square = square

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'
