import math

def cash_return_coro(percent: float, years: int) -> float:
    value = math.pow(1 + percent / 100, years)
    while True:
        try:
            deposit = (yield)
            yield round(deposit * value, 2)
        except GeneratorExit:
            print('Выход из корутины')
            raise


coro = cash_return_coro(5, 5)
next(coro)
values = [1000, 2000, 5000, 10000, 100000]
for item in values:
    print(coro.send(item))
    next(coro)
coro.close()
