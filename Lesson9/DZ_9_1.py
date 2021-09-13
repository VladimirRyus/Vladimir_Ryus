from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 3), ('Green', 10))
    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running()
