# итератор в отдельном классе

class Range:
    def __init__(self, stop_value):
        self.stop_value = stop_value
        self.current = -1

    def __iter__(self):
        print(self)
        return RangeIterator(self)


class RangeIterator:
    def __init__(self, container):
        self.container = container

    def __next__(self):
        if self.container.current < self.container.stop_value:
            self.container.current += 1
            return self.container.current
        raise StopIteration


_range = Range(5)
for i in _range:
    print(i)


# объект класса и итерабельный, и итератор

class Range2:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration


# цикл for под капотом

iterable = Range2(5)
iterator = iterable.__iter__()
while True:
    try:
        value = iterator.__next__()
        print(value)
    except StopIteration:
        break


iterable = Range2(5)
iterator = iter(iterable)
while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break
