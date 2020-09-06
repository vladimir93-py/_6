from time import sleep

class TrafficLight:
    __color = 'Black'

    def running(self):
        while True:
            print('TrafficLight Red')
            sleep(7)
            print('TrafficLight Yellow')
            sleep(2)
            print('TrafficLight Green')
            sleep(7)
            print('TrafficLight Yellow')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()