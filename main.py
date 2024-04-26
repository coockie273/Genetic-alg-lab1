from Population import Population


def func(x):
    return math.sin(x) / (1 + math.exp(-x))


print(Population(100, 1000, 0.5, 0.01, func).start())
