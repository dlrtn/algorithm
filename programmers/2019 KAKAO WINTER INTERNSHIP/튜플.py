import collections
import re


def solution(s):
    nums = re.findall(r'\d+', s)
    counter = collections.Counter(nums)
    answer = [int(num) for num, _ in counter.most_common()]
    return answer

# 정규식을 사용하여 문자열에서 숫자만 추출합니다. 따라서 문자열에서 배열을 분리하는 작업과 중복된 코드를 제거할 수 있습니다.
# collections.Counter를 사용하여 각 숫자가 나타난 횟수를 계산합니다. 이를 사용하면 딕셔너리를 만들고 값을 계산하는 것보다 간단하게 작성할 수 있습니다.
# 마지막으로 most_common() 메소드를 사용하여 가장 많이 등장한 숫자부터 리스트를 만듭니다. 이를 통해 sorted() 함수를 사용하는 것보다 더욱 간단하게 구현할 수 있습니다.