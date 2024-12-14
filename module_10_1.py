# Импорты необходимых модулей и функций
import time
import threading
# Объявление функции write_words
def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')
# Взятие текущего времени
time_start1 = time.time()
# Запуск функций с аргументами из задачи (после создания файла вызовите 4 раза функцию write_words)
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Взятие текущего времени
time_end1 = time.time()
# Вывод разницы начала и конца работы функций
time_res1 = time_end1 - time_start1
print (f'Работа потоков {time_res1}')
# Взятие текущего времени
time_start2 = time.time()
# Создание и запуск потоков с аргументами из задачи
thread1= threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# Взятие текущего времени
time_end2 = time.time()
# Вывод разницы начала и конца работы потоков
time_res2 = time_end2 - time_start2
print (f'Работа потоков {time_res2}')
