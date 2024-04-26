from ExtremumFinder import ExtremumFinder


def func(x):
    return math.sin(x) / (1 + math.exp(-x))


print(ExtremumFinder(100, 1000, 0.5, 0.01, func).start())
