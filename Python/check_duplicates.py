from typing import List
def check_duplicate(nums: List[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
print(check_duplicate(nums = [1, 2, 4, 1, 1]))