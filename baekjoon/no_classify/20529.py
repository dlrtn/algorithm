T = int(input())

for i in range(T):
    m = 100000
    N = int(input())
    temp = list(input().split())
    if N >= 33:
        print(0)
        continue
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    t = 0
                    if i == j or j == k or k == i:
                        continue
                    for a in range(4):
                        if temp[i][a] != temp[j][a]:
                            t += 1
                        if temp[j][a] != temp[k][a]:
                            t += 1
                        if temp[k][a] != temp[i][a]:
                            t += 1
                    m = min(m, t)

    print(m)
