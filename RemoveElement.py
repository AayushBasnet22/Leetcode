class Solution:
    def removeElement(self, nums: list[int], val: int) -> int: # 27
        if not nums:
             return 0
        else:
            last_index = len(nums) - 1
            print(last_index)
            i = 0
            while i < last_index:
                if nums[i] == val:
                    if nums[last_index] != val:
                        temp = nums[i]
                        nums[i] = nums[last_index]
                        nums[last_index] = temp
                        i += 1
                    last_index -= 1
                else:
                    i += 1
            return i + 1 if nums[i] != val else i