N = int(input())
nums = []
for i in range(N):
    [b, a] = map(int, input().split())
    nums.append([a, b])
nums.sort()
for i in range(N):
    print(nums[i][1], nums[i][0])