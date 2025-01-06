from datetime import datetime as dt
from multiprocessing import Pool

def read_info(name):
    all_data = []                   #Создание локального списка all_data
    with open(name, 'r') as f:      #Открытие файла name для чтения
        while True:                 #Считывать построчно, пока считанная строка не окажется пустой
            line = f.readline()
            all_data.append(line)   #Во время считывания добавлять каждую строку в список all_data
            if not line:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)] #список названий файлов

start_time = dt.now()                      #Вызов read_info для каждого файла по очереди (линейно)
for name in filenames:
    read_info(name)
end_time = dt.now()
print(end_time - start_time, '(линейный)') #Измерьте время выполнения и выведите его в консоль

if __name__ == '__main__':
    start_time = dt.now()
    with Pool(processes=4) as pool:   #Вызов read_info для каждого файла, при многопроцессном подходе
        pool.map(read_info, filenames) #метод map, передав в него функцию read_info и список файлов
    end_time = dt.now()
    print(end_time - start_time, '(многопроцессный)') #Измерьте время выполнения и выведите его в консоль