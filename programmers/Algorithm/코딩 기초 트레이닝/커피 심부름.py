def solution(order):
    answer = 0

    for i in order:
        if i in ["iceamericano", "americanoice"]:
            answer += 4500
        if i in ["hotamericano", "americanohot"]:
            answer += 4500
        if i in ["icecafelatte", "cafelatteice"]:
            answer += 5000
        if i in ["hotcafelatte", "cafelattehot"]:
            answer += 5000
        if i in ["americano"]:
            answer += 4500
        if i in ["cafelatte"]:
            answer += 5000
        if i in ["anything"]:
            answer += 4500

    return answer
