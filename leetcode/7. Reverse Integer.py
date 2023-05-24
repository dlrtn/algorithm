class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        # 0을 제거한 후 숫자 뒤집기
        reversed_num = int(str(x)[::-1])

        if reversed_num > 2147483647:
            return 0

        return -reversed_num if is_negative else reversed_num