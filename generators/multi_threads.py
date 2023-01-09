import time
import os

from threading import Thread, Lock

counter = 0

# Объект блокировки
lock = Lock()

def increment():
    global counter
    for i in range(2000000):
        # С помощью контекстного менеджера захватываем блокировку и отпускаем, как только выходим из него
        with lock:
            counter += int(1)


t = Thread(target=increment)
t.start()

t2 = Thread(target=increment)
t2.start()

t.join()
t2.join()
print(counter)
