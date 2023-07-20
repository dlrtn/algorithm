import math

def factorial_to_week(N):
    seconds = math.factorial(N)
    weeks = seconds // (7 * 24 * 60 * 60)

    return weeks

factorial_to_week(int(input()))