import time
class TrafficLight:

    __color__ = 'Красный'

    def running(self):
        print('Светофор включен!')

svetofor = TrafficLight()
svetofor.running()
i = 0
while i < 3:
    svetofor.__color__ = 'Красный'
    print(svetofor.__color__)
    time.sleep(7)
    svetofor.__color__ = "Жёлтый"
    print(svetofor.__color__)
    time.sleep(2)
    svetofor.__color__  = "Зелёный"
    print(svetofor.__color__)
    time.sleep(7)
    i = i + 1