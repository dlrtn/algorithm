def solution(k, tangerine):
    answer = 0

    ans = [0] * 10000001

    for i in tangerine:
        ans[i] += 1

    ans.sort()

    cnt = 1
    for i in list(reversed(ans)):
        k = k - i

        if k <= 0:
            return cnt
        cnt += 1
