class Road:
    def __init__(self, lenght, widnt):
        self._lenght = lenght
        self._widnt = widnt

    def get_full_profit(self):
        return f'{self._lenght} м * {self._widnt} м * 25кг * 5см = {(self._widnt * self._lenght * 25 * 5) / 1000}тонн'

road_1 = Road(100, 5)
print(road_1.get_full_profit())