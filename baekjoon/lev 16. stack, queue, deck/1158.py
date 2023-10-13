import sys

n, k = map(int, sys.stdin.readline().split())
queue = [i for i in range(1, n + 1)]
result = []
count = 0

for i in range(n):
    count += k - 1
    if count >= len(queue):
        count = count % len(queue)
    result.append(str(queue.pop(count)))
print("<", ", ".join(result), ">", sep='')
