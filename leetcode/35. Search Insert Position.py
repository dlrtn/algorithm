class MostReceivedGift:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target:
                if left == mid:
                    return left
                right = mid
            elif nums[mid] < target:
                if left == mid:
                    if nums[right] < target:
                        return right + 1
                    else :
                        return right
                left = mid
            else:
                return mid