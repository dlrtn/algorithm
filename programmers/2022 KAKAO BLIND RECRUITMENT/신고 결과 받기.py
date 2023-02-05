def solution(id_list, report, k):
    # 제재 유저
    ban_list = []

    # 신고 처리 결과를 저장하는 딕셔너리
    result_dic = {}

    # 중복 신고 제거
    report = set(report)
    report = list(report)

    # 결괏값 배열 초기화
    result = [0] * len(id_list)

    # 신고횟수 카운트 및 제재 유저 확인
    id_dic = {}
    for i in id_list:
        id_dic[i] = 0
        result_dic[i] = 0

    # 신고 처리
    for i in report:
        id_dic[i.split()[1]] += 1

    # 제재 리스트에 유저 추가
    for i in id_dic:
        if id_dic[i] >= k:
            ban_list.append(i)

    # 제재 유저가 신고한 유저에게 제재 횟수 추가
    for i in report:
        if i.split()[1] in ban_list:
            result_dic[i.split()[0]] += 1

    # 제재 횟수 배열로 변환
    return list(result_dic.values())