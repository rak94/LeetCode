from typing import List

class FirstLastElement:
    def searchElement(self, nums: List[int], target: int) -> List[int]:
        # first occurance
        leftVal = self.binarySearch(nums, target, True)
        # last occurance
        rightVal = self.binarySearch(nums, target, False)
        return [leftVal, rightVal]
    
    """ 
    binary search algorithm to find the target element
    return true if element is in leftBias, false if it is in rightBias
    """
    def binarySearch(self, nums: List[int], target: int, leftBias: bool):
        # initialize left and right pointers
        left, right = 0, len(nums) - 1
        # store result to -1
        res = -1
        # iterate through the array to find mid
        while left <= right:
            # find mid value
            mid = (left + right) // 2
            # search left or right to the mid
            if target > nums[mid]:
                # move left pointer to mid + 1
                left = mid + 1
            elif target < nums[mid]:
                # move right pointer to mid - 1
                right = mid - 1
            else:
                res = mid
                # find the firs and last occurance
                if leftBias:
                    # move right pointer before mid
                    right = mid - 1
                else:
                    # move left pointer after mid
                    left = mid + 1
        return res
