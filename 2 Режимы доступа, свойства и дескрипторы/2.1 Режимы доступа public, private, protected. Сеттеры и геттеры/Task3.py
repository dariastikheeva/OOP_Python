class Clock:
    def __init__(self, time):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time
    
    @staticmethod
    def __check_time(tm):
        return type(tm) is int and 0 <= tm < 100000
    
clock = Clock(0)
clock.set_time(4530)
