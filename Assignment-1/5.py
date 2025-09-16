import random
def random_num(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

print(random_num(10))