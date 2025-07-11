# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []                    # Stack to simulate recursion
        curr = root                   # Current node pointer

        while stack or curr:          # Continue while we have nodes to process
            while curr:               # Go as far left as possible
                stack.append(curr)    # Push current node to stack
                curr = curr.left      # Move to left child
            
            curr = stack.pop()        # Pop the leftmost unprocessed node
            k -= 1                    # We've visited one more node
            if k == 0:                # Found the kth smallest!
                return curr.val
            curr = curr.right         # Move to right subtree
