n = int(input())
for i in range(n):
    num, str = input().split()
    for j in str:
        for k in range(int(num)):
            print(j,end='')
    print()