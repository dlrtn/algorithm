import sys

str = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for i in range(len(str)):
    print(stack)
    stack.append(str[i])
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))