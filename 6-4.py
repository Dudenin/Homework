import random

class Car:

    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police= p

    def go(self):
        print("GO!")

    def stop(self):
        print('STOP!')

    def turn(self):
        print(random.choice(['Left', 'Right']))

    def info(self):
        print(f'{self.name} {self.color} {self.speed} km/h {self.is_police}')

    def show_speed(self):
        print(f'{self.speed} km/h')

class TownCar(Car):

    def show_speed(self):
        print(f'{self.speed} km/h')
        if self.speed > 60:
            print("ALARM!")

class SportCar(Car):

    def show_speed(self):
        print(f'{self.speed} km/h')
        if self.speed > 80:
            print("ALARM!")

class WorkCar(Car):
    def show_speed(self):
        print(f'{self.speed} km/h')
        if self.speed > 40:
            print("ALARM!")
class PoliceCar(Car):
    pass

auto_1 = WorkCar(50,'Green','Mazda', False)
auto_1.info()
auto_1.go()
auto_1.stop()
auto_1.turn()
auto_1.show_speed()
print('\n')

auto_2 = TownCar(150,'Yellow','BMW', False)
auto_2.info()
auto_2.go()
auto_2.stop()
auto_2.turn()
auto_2.show_speed()
print('\n')

auto_3 = SportCar(100,'Red','BMW', False)
auto_3.info()
auto_3.go()
auto_3.stop()
auto_3.turn()
auto_3.show_speed()

print('\n')
auto_4 = PoliceCar(100,'Red','BMW', True)
auto_4.info()
auto_4.go()
auto_4.stop()
auto_4.turn()
auto_4.show_speed()