class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)

        answer_list = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while True:
                    if left >= right:
                        break

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total > target:
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in answer_list:
                            answer_list.append([nums[i], nums[j], nums[left], nums[right]])
                        else:
                            pass
                        left += 1

        return answer_list
