import threading
class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if philosopher:
            left = self.forks[philosopher]
            right = self.forks[(philosopher - 1) % 5]
        else:
            left = self.forks[(philosopher - 1) % 5]
            right = self.forks[philosopher]
        with left:
            with right:
                pickLeftFork()
                pickRightFork()
                eat()
                putRightFork()
                putLeftFork()
        