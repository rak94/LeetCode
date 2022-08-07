from typing import List

class SubsetSolution:
    def subset(self, nums: List[int]) -> List[int]:
        resArr = []
        subsetArr = []

        def dfs(i):
            if i >= len(nums):
                resArr.append(subsetArr.copy())
                return
            
            subsetArr.append(nums[i])
            dfs(i + 1)

            subsetArr.pop()
            dfs(i + 1)

        dfs(0)
        return resArr
