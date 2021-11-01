n = int(input())
def move(fr, to):
    print(str(fr) + ' ' + str(to))

def rec(n, fr, by, to):
    if n==1:
        move(fr, to)
    else:
        rec(n-1, fr, to, by)
        move(fr, to)
        rec(n-1,by,fr,to)
print(2**n-1)
rec(n, 1, 2, 3)