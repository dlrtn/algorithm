class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        temp = []

        if len(s) == 0:
            return 0

        maxLen = 1

        while True:
            if left == len(s):
                break

            if s[left] in temp:
                left = temp.index(s[left]) + 1 + left - len(temp)
                temp = []

            temp.append(s[left])
            left += 1

            maxLen = max(maxLen, len(temp))
        return maxLen
