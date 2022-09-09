class Stationery:
    def __init__(self, t):
        self.title = t
    def draw(self):
        print(f'Это пишет {self.title}')
    def take(self):
        print(f'Берём {self.title}')

class Pen(Stationery):

    def draw(self):
        print("Эта надпись написана ручкой")

class Pensil(Stationery):

    def draw(self):
        print("Эта надпись написана карандашом")

class Handle(Stationery):

    def draw(self):
        print("Эта надпись написана маркером")


red_pen = Pen("Красная ручка")
red_pen.take()
red_pen.draw()

black_pencil = Pensil("Чёрный карандаш")
black_pencil.take()
black_pencil.draw()

blue_handle = Handle("Синий маркер")
blue_handle.take()
blue_handle.draw()