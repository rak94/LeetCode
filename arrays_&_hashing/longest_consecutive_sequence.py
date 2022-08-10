from typing import List

class LongestSequence:
    def longest_sequence(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in num:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest