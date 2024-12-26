def get_loss(w1, w2, w3, w4):
    try:
        w = 10 * w1 // w2
    except ZeroDivisionError:
        return 'деление на ноль'
    else:
        return w - 5 * w2 * w3 + w4
    