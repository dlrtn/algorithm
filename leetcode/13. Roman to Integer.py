class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        answer = 0

        while True:
            print(count)
            print(answer)
            if count + 1 > len(s):
                break

            if s[count] == 'I':
                if count + 1 < len(s) and s[count + 1] == 'V':
                    answer += 4
                    count += 2
                    continue
                elif count + 1 < len(s) and s[count + 1] == 'X':
                    answer += 9
                    count += 2
                    continue

            if s[count] == 'X':
                if count + 1 < len(s) and s[count + 1] == 'L':
                    answer += 40
                    count += 2
                    continue
                elif count + 1 < len(s) and s[count + 1] == 'C':
                    answer += 90
                    count += 2
                    continue

            if s[count] == 'C':
                if count + 1 < len(s) and s[count + 1] == 'D':
                    answer += 400
                    count += 2
                    continue
                elif count + 1 < len(s) and s[count + 1] == 'M':
                    answer += 900
                    count += 2
                    continue

            answer += dic[s[count]]
            count += 1

        return answer