# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:                              # Base case: empty node
                return 0

            res = 1 if node.val >= maxVal else 0     # Is current node good?
            maxVal = max(maxVal, node.val)           # Update max for children
            res += dfs(node.left, maxVal)            # Count good nodes in left subtree
            res += dfs(node.right, maxVal)           # Count good nodes in right subtree
            return res                               # Return total count

        return dfs(root, root.val)                   # Start DFS from root
