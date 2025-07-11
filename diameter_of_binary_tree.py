'''
Brute Force Method
For every node in the tree, compute the depth of its left and right subtrees. 
The diameter at that node is the sum of those depths. 
Compute this for every node and return the maximum diameter found.

Time Complexity: O(n²) (for each node, compute depth of subtrees which is O(n) per node)

Space Complexity: O(h) (recursion stack; h is the height of the tree)

def diameterOfBinaryTree(root):
    res = [0]  # Use list to allow modification in nested function

    def dfs(curr):
        if not curr:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        res[0] = max(res[0], left + right)  # Update max diameter
        return 1 + max(left, right)         # Return depth

    dfs(root)
    return res[0]

'''
'''
Optimal Method (Single DFS Traversal)
Use DFS to compute the depth of each subtree while 
updating the maximum diameter found so far. The diameter at any node 
is the sum of the depths of its left and right subtrees.

Time Complexity: O(n) (each node visited once)

Space Complexity: O(h) (recursion stack; h is the height of the tree)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        def dfs(curr):
            if not curr:
                return 0
            
            left=dfs(curr.left)
            right=dfs(curr.right)

            self.res=max(self.res,left+right)
            return 1 +max(left,right)
        dfs(root)
        return self.res
        