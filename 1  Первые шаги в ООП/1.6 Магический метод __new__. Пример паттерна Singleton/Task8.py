TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            d = DialogWindows()
            setattr(d, 'name', *args)
            return d
        else:
            d = DialogLinux()
            setattr(d, 'name', *args)
            return d
