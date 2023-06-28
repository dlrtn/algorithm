A = int(input())
B = int(input())
C = int(input())


sum = A + B + C

if sum != 180:
    print('Error')
else:
    if A == B == C:
        print('Equilateral')
    elif A == B or B == C or C == A:
        print('Isosceles')
    else:
        print('Scalene')