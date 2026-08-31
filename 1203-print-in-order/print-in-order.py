from typing import Callable
from threading import Event


class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        # Tell second() that first() has finished
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:

        # Wait until first() has finished
        self.first_done.wait()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        # Tell third() that second() has finished
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait until second() has finished
        self.second_done.wait()

        # printThird() outputs "third". Do not change or remove this line.
        printThird()