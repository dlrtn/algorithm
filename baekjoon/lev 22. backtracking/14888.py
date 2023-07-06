N = int(input())

arr = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_num = -1000000000
min_num = 1000000000

string = ''


def dfs(result, depth=1):
    global add, sub, mul, div, max_num, min_num

    if depth == len(arr):
        max_num = max(result, max_num)
        min_num = min(result, min_num)
        return

    else:
        if add > 0:
            add -= 1
            dfs(result + arr[depth], depth + 1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(result - arr[depth], depth + 1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(result * arr[depth], depth + 1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(result / arr[depth]), depth + 1)
            div += 1


dfs(arr[0])

print(max_num)
print(min_num)
