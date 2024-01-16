class MostReceivedGift:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        answer = 0
        result = 1000000000
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                m = abs(target - s)
                if m < result:
                    answer = s
                    result = m
                if s > target:
                    right -= 1

                elif s < target:
                    left += 1

                else:
                    return target
        return answer
