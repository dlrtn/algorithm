A, B, C = map(int, input().split())

def divide_conquer(A, B, C):
    if B == 1:
        return A % C
    else:
        temp = divide_conquer(A, B // 2, C)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C

print(divide_conquer(A, B, C))
