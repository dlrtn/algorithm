from collections import Counter


def has_special_chars(text):
    special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?~` "

    for char in text:
        if char in special_chars:
            return True
    return False


def has_number(text):
    for char in text:
        if char.isdigit():
            return True
    return False


def jaccard_similarity_multiset(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())
    return intersection / union


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = []
    set2 = []
    for i in range(len(str1) - 1):
        now_temp = str1[i:i + 2]
        if has_special_chars(now_temp) or has_number(now_temp):
            continue
        else:
            set1.append(now_temp)

    for i in range(len(str2) - 1):
        now_temp = str2[i:i + 2]
        if has_special_chars(now_temp) or has_number(now_temp):
            continue
        else:
            set2.append(now_temp)

    if len(set1) == 0 and len(set2) == 0:
        return 65536

    return int(jaccard_similarity_multiset(set1, set2) * 65536)
