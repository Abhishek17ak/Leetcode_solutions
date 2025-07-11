'''
Brute Force Method
Traverse the entire tree and, for each node, create a new node with the 
same value but with the left and right children swapped recursively. 
This builds a new inverted tree rather than modifying the original.

Time Complexity: O(n) (visit every node once)

Space Complexity: O(n) (space for the new tree and recursion stack)

def invertTree(root):
    if not root:
        return None
    new_root = TreeNode(root.val)
    new_root.left = invertTree(root.right)
    new_root.right = invertTree(root.left)
    return new_root

'''
'''
Optimal Method (In-Place Recursive Swap)
Recursively swap the left and right children of each node in the tree. 
This modifies the tree in place and requires only the recursion stack for extra space.

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

def invertTree(root):
    if not root:
        return None
    
    # Swap left and right children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    # Recursively invert left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    return root

        