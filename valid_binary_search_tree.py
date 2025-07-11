# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:                              # Base case: empty node
                return True

            if not (left < node.val < right):         # Check if node is in valid range
                return False
            
            # Check left subtree: values must be between left and node.val
            # Check right subtree: values must be between node.val and right
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))  # Start with infinite range
