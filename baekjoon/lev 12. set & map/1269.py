a,b = map(int,input().split())

a_arr = set(map(int,input().split()))
b_arr = set(map(int,input().split()))

print(len(b_arr-a_arr)+len(a_arr-b_arr))