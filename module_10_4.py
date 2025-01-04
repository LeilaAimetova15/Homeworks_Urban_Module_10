from threading import Thread
import random
from time import sleep
from queue import Queue

class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            guest_sat_down = False
            for i in range(len(self.tables)):
                if self.tables[i].guest is None: #проверка значения на None
                    self.tables[i].guest = guest
                    guest.start()
                    guest_sat_down = True
                    print(f'{guest.name} сел(-а) за стол номер {self.tables[i].number}')
                    break
            if not guest_sat_down:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        free_table = False
        while not self.queue.empty() or not free_table: #проверка пустоты очереди
            for i in range(len(self.tables)):
                if not self.tables[i].guest is None:
                    if not self.tables[i].guest.is_alive(): #проверка выполнения потока в текущий момент
                        print(f'{self.tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {self.tables[i].number} свободен')
                        if not self.queue.empty():
                            self.tables[i].guest = self.queue.get()
                            print(f'{self.tables[i].guest.name} вышел(-ла) из очереди и сел(-а) '
                              f'за стол номер {self.tables[i].number}')
                            self.tables[i].guest.start()
                        else:
                            self.tables[i].guest = None
                            free_table = True
                else:
                    free_table = True

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()