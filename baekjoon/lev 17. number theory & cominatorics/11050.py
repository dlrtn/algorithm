a, b = map(int, input().split())

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(int(fac(a)/(fac(b)*fac(a-b))))