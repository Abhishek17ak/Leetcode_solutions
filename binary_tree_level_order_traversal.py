'''
Optimal Method (Using Queue for BFS)
Use a queue to process nodes level by level. For each level, 
process all nodes currently in the queue, collect their values, 
and enqueue their children for the next level.

Time Complexity: O(n) (each node is processed once)

Space Complexity: O(n) (queue and result list)
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []                    # Final result: list of levels
        q = collections.deque()     # Queue to store nodes to visit
        q.append(root)              # Start with the root

        while q:                    # While there are nodes to process
            qLen = len(q)           # How many nodes are at current level
            level = []              # List to store current level's values
            
            for i in range(qLen):   # Process all nodes at current level
                node = q.popleft()  # Take the first node from queue
                if node:            # If node exists (not None)
                    level.append(node.val)      # Add its value to current level
                    q.append(node.left)         # Add left child to queue
                    q.append(node.right)        # Add right child to queue
            
            if level:               # If current level has any values
                res.append(level)   # Add this level to final result
                
        return res
