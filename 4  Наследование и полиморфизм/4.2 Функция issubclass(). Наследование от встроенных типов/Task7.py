class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating(object):
    MIN_RATING = 0
    MAX_RATING = 5

    def __init__(self, rating=0):
        self.__rating = rating

    def __setattr__(self, key, value):
        if key == 'rating':
            if (
                not isinstance(value, int)
                or (value < self.MIN_RATING)
                or (value > self.MAX_RATING)
            ):
                raise ValueError('неверное присваиваемое значение')
        object.__setattr__(self, key, value)

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, value):
        self.__rating = value
