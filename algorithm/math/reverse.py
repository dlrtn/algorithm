import numpy as np

lit = list(map(int, input().split()))
lst = list(map(int, input().split()))

A = np.array([lit[:3], lit[3:6], lit[6:]])

if np.linalg.matrix_rank(A) < A.shape[0]:
    print("Matrix A is singular. Inverse does not exist.")
else:
    A_1 = np.linalg.inv(A)
    print("Inverse of matrix A:")
    print(A_1)

    print("MostReceivedGift of linear equations:")
    print(np.dot(A_1, lst))