def solution(people, limit):

    people = sorted(people) # 데이터를 정렬

    answer = 0 # 구명보트를 카운트 갯수

    left = 0 # 투 포인터를 사용하여 접근
    right = len(people) - 1

    while True:

        if left > right:
            break

        if people[left] + people[right] > limit: # 문제에서 구명보트는 최대 2명만 태울 수 있다 했으니 사용 가능한 방법
            answer += 1
            right -= 1
        else :
            answer += 1
            left += 1
            right -= 1

    return answer
