'''
Brute Force Method (for any binary tree)
Traverse the tree from the root.

For each node, check if both p and q exist in the left and right subtrees.

If one is found in the left and the other in the right (or vice versa), the current node is the LCA.

If both are on the same side, recurse on that subtree.

Time Complexity: O(n) (must potentially visit all nodes)

Space Complexity: O(h) (recursion stack, h = tree height)

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

'''
'''
So, starting from the root:

If both p and q are greater than the current node, move to the right child.

If both are less, move to the left child.

If they split (one on each side, or one equals the current node), the current node is their LCA.

Time Complexity: O(h) (h = height of the tree; O(log n) for balanced, O(n) for skewed)

Space Complexity: O(1) (iterative), O(h) (recursive stack)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root                              # Start from root
        
        while cur:                              # Traverse until we find LCA
            if p.val > cur.val and q.val > cur.val:    # Both nodes are in right subtree
                cur = cur.right                 # Go right
            elif p.val < cur.val and q.val < cur.val:  # Both nodes are in left subtree
                cur = cur.left                  # Go left
            else:                               # Found the LCA
                return cur


        
        