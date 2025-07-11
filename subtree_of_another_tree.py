'''
Brute Force Method
For every node in the main tree root, check if the subtree rooted at that node is identical to subRoot using a helper function that compares two trees for structural and value equality.

Time Complexity: O(m * n), where m is the number of nodes in root and n is the number of nodes in subRoot
(for each node in root, you may compare up to all nodes in subRoot)

Space Complexity: O(h), where h is the height of the tree (recursion stack)

'''
'''
Optimal Method
The above approach is already optimal for the constraints (tree size ≤ 100). 
For larger trees, you could use hashing or serialization to optimize subtree comparison, 
but for this size, the recursive method is efficient and clear.

Time Complexity: O(m * n)

Space Complexity: O(h)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True #if subtree is null then null is a part of normal tree
        if not root:
            return False # if tree is null then there cant be subtree

        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot)or self.isSubtree(root.right,subRoot))


        
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
        return False    
        