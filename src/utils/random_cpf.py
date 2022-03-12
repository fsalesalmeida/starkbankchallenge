import random


def generate():
    def make_digit(digs):
        s = 0
        qtd = len(digs)
        for i in range(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10:
            return 0
        return res

    n = [random.randrange(10) for i in range(9)]
    n.append(make_digit(n))
    n.append(make_digit(n))
    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)
