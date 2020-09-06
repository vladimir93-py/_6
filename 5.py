class Stationery:
    def __init__(self, title='рисовать!!'):
        self.title = title

    def draw(self):
        print(f'Можешь начать {self.title}))')

class Pencil(Stationery):
    def draw(self):
        print(f'Начни рисовать {self.title} карандашом!')

class Pen(Stationery):
    def draw(self):
        print(f'Начни рисовать {self.title} ручкой!')

class Marker(Stationery):
    def draw(self):
        print(f'Начни рисовать {self.title} маркером!')

start = Stationery()
start.draw()
pen = Pen('черной гелевой')
pen.draw()
pencil = Pencil('BIGовским')
pencil.draw()
marker = Marker('красным или синим')
marker.draw()