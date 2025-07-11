'''
Brute Force & Optimal Method (Recursive Comparison)
For this problem, the brute force and optimal approaches are essentially the same:
Recursively check if both trees are structurally identical and have the same node values.

Steps:
If both nodes are None, return True.

If only one is None, return False.

If both nodes exist, check if their values are equal.

Recursively check the left and right subtrees.

Time Complexity: O(n), where n is the number of nodes (each node is visited once)

Space Complexity: O(h), where h is the height of the tree (recursion stack; O(log n) for balanced, O(n) for skewed)

Optimal Code (With Short Comments):
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False