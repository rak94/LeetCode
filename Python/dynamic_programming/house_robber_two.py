from typing import List

class HouseRobberTwo:
    def rob_house(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_help(nums[1:]), self.rob_help(nums[:-1]))

    def rob_help(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2