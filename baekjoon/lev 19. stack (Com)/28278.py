class Stack:

    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


N = int(input())

stack = Stack()
outputs = []

# 모든 입력을 먼저 받기
for _ in range(N):
    temp = input()

    if len(temp) > 1:
        stack.push(int(temp[2:]))
    elif temp[0] == '2':
        outputs.append(str(stack.pop()))
    elif temp[0] == '3':
        outputs.append(str(stack.size()))
    elif temp[0] == '4':
        outputs.append(str(stack.empty()))
    elif temp[0] == '5':
        outputs.append(str(stack.top()))

# 한 번에 출력 처리
print("\n".join(outputs))
