class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.title}: {self.width}, {self.height}')

    @property
    def title(self):
        return self.__title

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) == int and 0 <= width <= 10000:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) == int and 0 <= height <= 10000:
            self.__height = height
            self.show()
