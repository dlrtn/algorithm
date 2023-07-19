N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = 2 ** (N-1)
    if r < size <= c:  # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size > c:  # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:  # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

pos = 2 * r + c
cnt += pos

print(cnt)
