from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, nums, n = set(), sorted(nums), len(nums)
        numDict = {num: i for i, num in enumerate(nums)}
        i = bisect_left(nums, target - nums[n-1] * 3, 0, n)
        right1 = bisect_right(nums, target / 4, i, n)
        while i < right1:
            end2 = bisect_right(nums, target - nums[i] * 3, i + 1, n)
            target2 = target - nums[i]
            j = bisect_left(nums, target2 - nums[end2-1] * 2, i + 1, end2)
            right2 = bisect_right(nums, target2 / 3, j, end2)
            while j < right2:
                end3 = bisect_right(nums, target2 - nums[j] * 2, j + 1, n)
                target3 = target2 - nums[j]
                k = bisect_left(nums, target3 - nums[end3-1], j + 1, end3)
                right3 = bisect_right(nums, target3 / 2, k, end3)
                while k < right3:
                    target4 = target3 - nums[k]
                    if (target4 in numDict) and (numDict[target4] > k):
                        res.add((nums[i], nums[j], nums[k], target4))
                    k = numDict[nums[k]] + 1
                j = numDict[nums[j]] + 1
            i = numDict[nums[i]] + 1
        return res

    def fourSumWithoutBisect(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return nums

        nums = sorted(nums)
        nums_len = len(nums)
        res = []
        i = 0
        while i < nums_len:
            j = i+1
            while j < nums_len:
                target_2 = target - nums[j] - nums[i]
                front = j+1
                back = nums_len - 1
                while front < back:
                    two_sum = nums[front] + nums[back]
                    if two_sum < target_2:
                        front += 1
                    elif two_sum > target_2:
                        back -= 1
                    else:
                        res.append([nums[i], nums[j], nums[front], nums[back]])
                        while front < back and nums[front] == res[-1][2]:
                            front += 1
                        while front < back and nums[back] == res[-1][3]:
                            back -= 1
                while j+1 < nums_len and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            while i+1 < nums_len and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return res


print(Solution().fourSum([5, 5, 3, 5, 1, -5, 1, -2],
                         4))
