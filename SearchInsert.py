class Solution:
       def searchInsert(self, nums: list[int], target: int) -> int: # 35
        for index, number in enumerate(nums):
            if target <= number:
                return index
        return index + 1