class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []                    # Final result: rightmost nodes
        q = deque([root])          # Queue to store nodes to visit

        while q:                   # While there are nodes to process
            rightSide = None       # Track the rightmost node at current level
            qLen = len(q)          # How many nodes are at current level

            for i in range(qLen):  # Process all nodes at current level
                node = q.popleft() # Take the first node from queue
                if node:           # If node exists (not None)
                    rightSide = node              # Update rightmost node
                    q.append(node.left)          # Add left child to queue
                    q.append(node.right)         # Add right child to queue
            
            if rightSide:          # If we found a rightmost node at this level
                res.append(rightSide.val)  # Add its value to result
        
        return res
