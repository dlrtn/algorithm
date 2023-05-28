class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        if num >= 1000:
            answer += (num // 1000) * "M"
            num %= 1000
        if num >= 500:
            if num >= 900:
                answer += "CM"
                num %= 900
            else:
                answer += "D"
                num %= 500
        if num >= 100:
            if num >= 400:
                answer += "CD"
                num %= 400
            else:
                answer += (num // 100) * "C"
                num %= 100
        if num >= 50:
            if num >= 90:
                answer += "XC"
                num %= 90
            else:
                answer += "L"
                num %= 50
        if num >= 10:
            if num >= 40:
                answer += "XL"
                num %= 40
            else:
                answer += (num // 10) * "X"
                num %= 10
        if num >= 5:
            if num >= 9:
                answer += "IX"
                num %= 9
            else:
                answer += "V"
                num %= 5
        if num >= 1:
            if num >= 4:
                answer += "IV"
                num %= 4
            else:
                answer += (num // 1) * "I"

        return answer