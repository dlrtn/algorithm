n = int(input())


def find_next_prime(x):
    while True:
        if is_prime(x):
            return x
        else:
            x += 1


def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in range(n):
    target = int(input())
    print(find_next_prime(target))
