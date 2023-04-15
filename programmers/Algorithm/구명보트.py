def solution(people, limit):

    people = sorted(people) # �����͸� ����

    answer = 0 # ����Ʈ�� ī��Ʈ ����

    left = 0 # �� �����͸� ����Ͽ� ����
    right = len(people) - 1

    while True:

        if left > right:
            break

        if people[left] + people[right] > limit: # �������� ����Ʈ�� �ִ� 2�� �¿� �� �ִ� ������ ��� ������ ���
            answer += 1
            right -= 1
        else :
            answer += 1
            left += 1
            right -= 1

    return answer
