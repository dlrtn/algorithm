n = int(input())
stack = []
cnt = 0
for i in range(n):
    str = input()
    if len(str) % 2 == 1:
        print("NO")
        continue
    for j in str:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()
                cnt += 1
    if cnt == (len(str) // 2):
        print("YES")
    else :
        print("NO")
    cnt = 0

    stack.clear()