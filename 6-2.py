class MyRoad:

    def __init__(self, l, w):
        self._length_ = l
        self._width_ = w

    def building(self):
        print(self._length_*self._width_*25*5)

way = MyRoad(100, 10)
way.building()

