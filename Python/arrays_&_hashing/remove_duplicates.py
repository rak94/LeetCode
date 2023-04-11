from typing import List

class RemoveDuplicates:
    def remove_duplicates(self, nums: List) -> int:
        # initialize a pointer
        left = 1
        if nums == 0:
            return 0
        for i in range(1, len(nums)):
            # check if current value is equal to previous value
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                # increment left pointer
                left += 1
        return left