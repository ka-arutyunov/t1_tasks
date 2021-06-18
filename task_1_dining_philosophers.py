from random import randint
from threading import Thread, Lock
from time import sleep

forks = [Lock() for _ in range(5)]


def dining_philosophers(philosopher):
    first, last = min(philosopher, (philosopher + 1) % 5), max(philosopher, (philosopher + 1) % 5)
    while True:
        print(f'Философ: {philosopher} ожидает когда освободится первая вилка')
        with forks[first]:
            print(f'Философ: {philosopher} ожидает когда освободится вторая вилка')
            with forks[last]:
                sleep(randint(0, 2))  # Едят произвольное кол-во секунд от 0 до 2


philosophers = [Thread(target=dining_philosophers, args=(philosopher,)) for philosopher in range(5)]

for p in philosophers:
    p.start()
for p in philosophers:
    p.join()
