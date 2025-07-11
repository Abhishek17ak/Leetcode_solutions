class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]            # Adjacency list
        visit = [False] * n                     # Track visited nodes
        
        # Build adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):                          # Explore entire component
            for nei in adj[node]:               # Check all neighbors
                if not visit[nei]:              # If neighbor not visited
                    visit[nei] = True           # Mark as visited
                    dfs(nei)                    # Recursively explore
        
        res = 0                                 # Count components
        for node in range(n):                   # Check every node
            if not visit[node]:                 # Found new component
                visit[node] = True              # Mark starting node
                dfs(node)                       # Explore entire component
                res += 1                        # Increment component count
        return res                              # Fixed: was 'rese'
'''
Time and Space Complexity
Time Complexity: O(V + E)

V = number of vertices (nodes)

E = number of edges

Each node and edge visited exactly once

Space Complexity: O(V + E)

Adjacency list: O(V + E)

Visited array: O(V)

Recursion stack: O(V) in worst case'''