import threading

class Foo:
    def __init__(self):
        self.firstjob = threading.Lock()
        self.secondjob = threading.Lock()
        self.firstjob.acquire()
        self.secondjob.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstjob.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstjob:
            printSecond()
            self.secondjob.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondjob:
            printThird()