a, b = map(int, input().split())


def remainder_theorem(a, b):
    if a % b == 0:
        return b

    return remainder_theorem(b, a % b)


print(remainder_theorem(a, b))
