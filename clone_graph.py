'''
Optimal Method (BFS Iterative)
Use Breadth-First Search (BFS) with a queue to traverse the graph level by level. Clone nodes as you discover them and maintain a mapping from original to cloned nodes.

Time Complexity: O(V + E), where V is vertices and E is edges (each node and edge visited once)

Space Complexity: O(V) for the hash map and queue
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:                              # Handle empty graph
            return None

        oldToNew = {}                             # Map: original node → cloned node
        oldToNew[node] = Node(node.val)          # Clone the starting node
        q = deque([node])                        # Queue for BFS

        while q:                                 # BFS to visit all nodes
            cur = q.popleft()                    # Get next node to process
            for nei in cur.neighbors:            # Check all neighbors
                if nei not in oldToNew:          # If neighbor not cloned yet
                    oldToNew[nei] = Node(nei.val)  # Clone the neighbor
                    q.append(nei)                # Add to queue for processing
                oldToNew[cur].neighbors.append(oldToNew[nei])  # Connect cloned nodes

        return oldToNew[node]                    # Return cloned starting node
