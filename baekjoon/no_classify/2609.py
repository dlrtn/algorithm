a, b = map(int, input().split())
def max(n,m):
    if m>n :
        m,n = n,m
    while m != 0 :
        n = n%m
        n,m = m,n
    return n    
def min(n,m):
	return n*m // max(n,m)
print(max(a,b))
print(min(a,b))