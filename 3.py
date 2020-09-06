class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Profit': wage, 'Bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

manager = Position('Иван', 'Иванович', 'Иванов', 1000000, 250000)
print(manager.position)
print(manager.get_full_name())
print(manager.get_full_profit())