class Car:

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.police = police
        print(f'New car: {self.name} (color {self.color}) police_car - {self.police}')

    def go(self):
        print(f'{self.name}: car go-go-go!')

    def stop(self):
        print(f'{self.name}: car stop')

    def turn(self, direction):
        print(f'{self.name}: the car turned: {"Left" if direction == 0 else "Right"}.')

    def show_speed(self):
        return f'{self.name}: speed car: {self.speed}.'

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: speed car: {self.speed}. over speed!' \
            if self.speed > 60 else f'{self.name}: speed car {self.speed}'

class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: speed car: {self.speed}. over speed!' \
            if self.speed > 120 else f'{self.name}: speed car {self.speed}'


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: speed car: {self.speed}. over speed!' \
            if self.speed > 40 else f'{self.name}: speed car {self.speed}'

class PoliceCar(Car):

    def show_speed(self):
        return f'{self.name}: speed car: {self.speed}. over speed!' \
            if self.speed > 80 else f'{self.name}: speed car {self.speed}'


police = PoliceCar('Cops', 'black-white', 80)
police.go()
police.turn(0)
print(police.show_speed())
police.stop()

town_car = TownCar('MINI', 'blue', 60)
town_car.go()
town_car.turn(2)
print(town_car.show_speed())
town_car.stop()

sport_car = SportCar('Flash', 'yellow', 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()

work_car = WorkCar('Truck', 'red', 40)
work_car.go()
work_car.turn(5)
print(work_car.show_speed())
work_car.stop()

print(f'\nCar {town_car.name} (color {town_car.color}')
print(f'Car {police_car.name } (color {PoliceCar.color})')
