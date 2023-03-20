def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if i <= citations[i] and (len(citations) - i) >= citations[i]:
            answer = i
    return answer

a = list(map(int, input().split()))
print(a[solution(a)])
