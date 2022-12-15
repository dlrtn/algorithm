def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if i == j or j == k or i == k:
                    continue
                cnt = 0
                s = nums[i] + nums[j] + nums[k]

                for x in range(2, s):
                    if s % x == 0:
                        cnt += 1

                if cnt == 0:
                    answer += 1

    return answer