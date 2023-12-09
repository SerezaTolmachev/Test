import time


class Cat:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        self.energy = 100

    def sleep(self):
        print(f'Кот {self.name} уснул.')
        time.sleep(3)
        print(f'Кот {self.name} проснулся.')
        self.energy = 100

    def play(self):
        print(f'Ты начал играть с {self.name}.')
        r = int(input('Сколько раз будешь играть?'))
        self.energy -= r


cat = Cat('Boris', 'black', 7)
cat.play()
cat.sleep()
cat2 = Cat('Vasya', 'white', 13)
cat2.play()
cat2.sleep()


