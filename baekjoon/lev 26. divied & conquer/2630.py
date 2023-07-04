N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

def check(n, x, y):
    global b_count
    global w_count

    count = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] == 1:
                count += 1

    if count == n * n:
        b_count += 1
    elif count == 0:
        w_count += 1
    else:
        check(n // 2, x, y)
        check(n // 2, x, y + n // 2)
        check(n // 2, x + n // 2, y)
        check(n // 2, x + n // 2, y + n // 2)


b_count = 0
w_count = 0

check(N, 0, 0)

print(w_count)
print(b_count)
