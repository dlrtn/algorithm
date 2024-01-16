def solution(want, number, discount):
    answer = 0

    want_dic = dict()

    for i in range(len(want)):
        want_dic[want[i]] = i

    temp = [0] * len(want)

    for i in range(10):
        if discount[i] in want_dic:
            temp[want_dic[discount[i]]] += 1

    if temp == number:
        answer += 1

    for i in range(10, len(discount)):
        if discount[i - 10] in want_dic:
            temp[want_dic[discount[i - 10]]] -= 1

        if discount[i] in want_dic:
            temp[want_dic[discount[i]]] += 1

        if temp == number:
            answer += 1

    return answer

#solution 함수는 want, number, discount 세 개의 리스트를 입력으로 받습니다. 함수는 정수형 결과값을 반환합니다.
#먼저 want_dic이라는 빈 딕셔너리를 생성합니다. 이 딕셔너리는 want 리스트의 값을 키로 사용하고, 해당 값의 인덱스를 값으로 저장합니다.
#temp라는 길이가 want 리스트와 같은 길이인 0으로 초기화된 리스트를 생성합니다. temp 리스트는 각 아이템의 수량을 저장하는 용도로 사용됩니다.
#첫 10개의 할인에 대해서 want_dic에서 해당하는 아이템의 인덱스를 찾고, temp 리스트에서 해당 인덱스의 값을 1 증가시킵니다. 이 과정을 반복합니다.
#temp 리스트와 number 리스트가 동일하다면, 모든 아이템의 수량이 일치한다는 의미이므로 answer 값을 1 증가시킵니다.
#10번째 할인 이후부터는 동일한 방식으로 처리합니다. 현재 할인에서 제외되는 아이템의 인덱스를 찾아 해당 인덱스의 값을 1 감소시키고, 새로 추가되는 아이템의 인덱스를 찾아 해당 인덱스의 값을 1 증가시킵니다.
#이 과정에서 temp 리스트와 number 리스트가 동일하다면, 모든 아이템의 수량이 일치한다는 의미이므로 answer 값을 1 증가시킵니다.
#최종적으로 answer 값을 반환합니다.