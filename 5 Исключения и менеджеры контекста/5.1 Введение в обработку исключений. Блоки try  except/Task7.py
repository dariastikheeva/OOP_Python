# считывание строки и разбиение ее по пробелам
lst_in = input().split()

def check_text_on_integer(text):
    try:
        val = int(text)
        return True
    except:
        return False


res = sum(map(int, filter(check_text_on_integer, lst_in)))
print(res)
