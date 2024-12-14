import threading
import time
# Создание класса
class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)        # также можно исп-ть super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day_battle = 0
        while enemy > 0:
            day_battle += 1
            time.sleep(1)
            enemy -= self.power
            print(f'{self.name} сражается {day_battle} день(дня), осталось {enemy} воинов.\n')
        print(f'{self.name} одержал победу спустя {day_battle} дней(дня)!\n')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')