#every node connected or one-more nodes unconnected then not a tree, must be without cycle
#use dfs and get all visited nodes
#if visited nodes=n then true
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Quick check: tree must have exactly n-1 edges
        if len(edges) > (n - 1):
            return False
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()                           # Track visited nodes
        
        def dfs(node, par):                     # DFS to detect cycles
            if node in visit:                   # Already visited → cycle detected
                return False
            
            visit.add(node)                     # Mark as visited
            for nei in adj[node]:               # Check all neighbors
                if nei == par:                  # Skip parent (where we came from)
                    continue
                if not dfs(nei, node):          # Recursively check neighbor
                    return False                # Cycle found in subtree
            return True                         # No cycle found
        
        # Check: no cycles AND all nodes connected
        return dfs(0, -1) and len(visit) == n

        
        