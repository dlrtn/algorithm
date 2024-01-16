class MostReceivedGift:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        if arr == list(reversed(arr)):
            return True
        return False