from threading import *
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = hello()
t2 = hi()

t1.start()
sleep(.2)
t2.start()
sleep(.2)

t1.join()
t2.join()

print("Bye")  # part of main thread
