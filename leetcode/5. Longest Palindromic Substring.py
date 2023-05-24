class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s) - 1

        while True:
            for i in range(len(s) - n + 1):
                if self.isPalindrome(s[i:i + n + 1]):
                    return s[i:i + n + 1]

            n -= 1

            if n == 0:
                break
