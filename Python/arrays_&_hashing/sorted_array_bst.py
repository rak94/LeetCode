from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class ArrayToBst:
    def sorted_array_bst(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = build_bst(left, mid - 1)
            node.right = build_bst(mid + 1, right)

            return node
        
        return build_bst(0, len(nums) - 1)