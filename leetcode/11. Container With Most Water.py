class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height) - 1

        while left < right:
            answer = max(answer, min(height[right], height[left]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else :
                left += 1

        return answer