'''
Brute Force Method
For every node, compute the height of its left and right subtrees. If the difference in heights is more than 1, the tree is not balanced. Recursively check this for every node.

Time Complexity: O(n²) (for each node, height is computed recursively which is O(n) per node)

Space Complexity: O(h) (recursion stack; h is the height of the tree)

def isBalanced(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

'''
'''
Optimal Method (DFS with Early Termination)
Use DFS to compute the height of each subtree and check balance at the same time. 
Return both whether the subtree is balanced and its height. If any subtree is unbalanced, 
propagate False up the recursion.

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
def isBalanced(root):
    def dfs(node):
        if not node:
            return [True, 0]  # [is_balanced, height]
        
        left = dfs(node.left)      # Get left subtree info
        right = dfs(node.right)    # Get right subtree info
        
        # Check if current node is balanced
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        
        # Return [is_balanced, height_of_current_subtree]
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]  # Return only the balanced status