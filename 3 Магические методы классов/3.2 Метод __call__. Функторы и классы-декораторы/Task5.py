class DigitRetrieve:
    def __call__(self, *args, **kwds):
        return int(args[0]) if args[0].isdigit() or args[0][1:].isdigit() else None