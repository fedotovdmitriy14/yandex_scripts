import typing
from time import sleep


class CyclicIterator:
    def __init__(self, iterable: typing.Union[list, tuple, set, range]):
        self.iterable = iterable
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = None
        try:
            value = self.iterable[self.current]
        except IndexError:
            self.current = 1
            value = self.iterable[0]
        else:
            self.current += 1
        finally:
            sleep(1.0)
            return value




cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
