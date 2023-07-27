import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


T = int(input())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    answer = -1
    temp = x
    while temp <= lcm(M, N):
        if (temp - x) % M == 0 and (temp - y) % N == 0:
            answer = temp
            break
        temp += M

    print(answer)
