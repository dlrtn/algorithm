N = int(input())
nums = []
for i in range(N):
    [a, b] = map(str, input().split())
    nums.append([a, b])
a = sorted(nums, key = lambda x:x[0])
for i in a:
    print(i[0], i[1])