import sys

N = int(sys.stdin.readline().rstrip())

number_list = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []
count = 1
for i in range(N):
    if number_list[i] == count:
        count += 1
        while stack and stack[-1] == count:
            stack.pop()
            count += 1
    else:
        stack.append(number_list[i])

if stack:
    print("Sad")
else:
    print("Nice")

