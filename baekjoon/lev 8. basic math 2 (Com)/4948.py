import math

# 소수의 집합을 구함
nums = {x for x in range(2, 246_913) if x == 2 or x % 2 ==1}
# nums = 2와 홀수로 이루어진 집합
for odd_num in range(3, int(math.sqrt(246_912))+1, 2):  # 3부터 최대값의 제곱근까지 홀수만
    nums -= {i for i in range(2 * odd_num, 246_913, odd_num) if i in nums}
    # 홀수의 배수로 이루어진 집합을 생성해서 빼줌

# 반복문 만들기
while True:
    n = int(input())
    if n == 0:
        break  # n == 0 이면 반복문을 끝냄
    sosu_list = [i for i in range(n+1, 2*n+1) if i in nums]
    # 소수 집합(nums)안에서 n보다 크고 2*n보다 작거나 같은 수의 리스트를 생성
    print(len(sosu_list))