# считывание строки и разбиение ее по пробелам
lst_in = input().split()

def get_value(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(get_value, lst_in))
