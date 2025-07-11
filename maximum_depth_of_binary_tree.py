'''
Traverse every node in the tree, and for each node, 
recursively compute the depth of its left and right subtrees. 
The depth is 1 plus the maximum of the left and right subtree depths.

Time Complexity: O(n) (each node is visited once)

Space Complexity: O(h), where h is the height of the tree 
(recursion stack; O(log n) for balanced, O(n) for skewed)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        