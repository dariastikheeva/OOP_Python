import sys

# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

players = []

for pl in lst_in:
    pl = pl.split(';')
    player = Player(pl[0], int(pl[1]), int(pl[2]))
    players.append(player)

players_filtered = list(filter(bool, players))
