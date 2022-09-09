class Worker:

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income_ = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def getfullname(self):
        print(f'{self.name} {self.surname} {self.position}')

    def gettotalincome(self):
        print(self._income_['bonus'] + self._income_['wage'])

worker1 = Position('Ivan', 'Petrov', 'Manager', 100, 20)
worker2 = Position('Yaroslav', 'Ivanov', 'Programmer', 120, 10)

print('\nWorker:')
worker1.getfullname()
print('\nTotal income:')
worker1.gettotalincome()
print('\nWorker:')
worker2.getfullname()
print('\nTotal income:')
worker2.gettotalincome()
