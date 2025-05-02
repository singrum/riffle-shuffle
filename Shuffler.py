

from random import randint


class Shuffler:
    def __init__(self, size):
        self.size = size
        self.cut = size // 2
        self.shuffle_cnt = 0
        self.cards = [''] * self.size
        self.label()

    def make_equilibrium(self):
        while not self.is_equilibrium():
            self.shuffle()

    def is_equilibrium(self):
        return len(set(self.cards)) == self.size

    def shuffle(self):
        parts = self.cards[:self.cut], self.cards[self.cut:]
        self.cards = []

        while parts[0] and parts[1]:
            random = randint(0, 1)
            card = parts[random].pop()
            self.cards.append(card)

        self.cards.extend(parts[0])
        self.cards.extend(parts[1])
        self.label()

        self.shuffle_cnt += 1

    def label(self):
        for i in range(self.cut):
            self.cards[i] += "H"
        for i in range(self.cut, self.size):
            self.cards[i] += "T"
