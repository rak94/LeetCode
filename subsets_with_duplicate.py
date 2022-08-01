from typing import List

class SubsetDuplicate:
    def subsets_with_duplicate(self, nums: List[int]) -> List[int]:
        resArr = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                resArr.append(subset[::])
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return resArr