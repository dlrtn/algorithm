import sys

N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
stack = []

answer = [-1 for _ in range(N)]

for i in range(N): # N번 반복
    while stack and input_list[stack[-1]] < input_list[i]: # 스택이 비어있지 않고, 스택의 마지막 값이 현재 값보다 작은 동안 지금의 값으로 answer 배열을 채워나간다.
        answer[stack.pop()] = input_list[i]
    stack.append(i) # 스택에 현재 인덱스를 넣는다.

print(*answer)
