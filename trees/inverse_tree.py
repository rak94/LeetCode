class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class TreeInverse:
    def inverse_tree(self, root):
        if not root:
            return None

        # swap tree children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.inverse_tree(root.left)
        self.inverse_tree(root.right)
        return root