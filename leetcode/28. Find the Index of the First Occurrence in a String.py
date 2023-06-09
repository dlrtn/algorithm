class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        index = 0
        while (index <= len(haystack)-len(needle)):
            if haystack[index:index+len(needle)] == needle:
                return index
            index += 1
        return -1