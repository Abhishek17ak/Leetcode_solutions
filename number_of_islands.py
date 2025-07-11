'''
Optimal Method (BFS/DFS Flood Fill)
Traverse each cell in the grid.

When an unvisited land cell is found, perform BFS (or DFS) 
to mark all connected land cells as visited (change them to '0').

Each BFS/DFS call corresponds to discovering a new island.

Time Complexity: O(m × n) (every cell is visited at most once)

Space Complexity: O(min(m, n)) for DFS recursion stack (worst case: a long narrow island), or O(m × n) for BFS queue in the worst case (all land).
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:                                  # Handle empty grid
            return 0
        
        rows, cols = len(grid), len(grid[0])         # Get grid dimensions
        islands = 0                                   # Counter for islands
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # 4 directions: down, up, right, left

        def bfs(r, c):                               # Explore entire island using BFS
            q = deque()
            grid[r][c] = "0"                         # Mark starting cell as visited
            q.append((r, c))
            
            while q:                                 # Process all connected land
                row, col = q.popleft()
                for dr, dc in directions:            # Check all 4 neighbors
                    nr, nc = dr + row, dc + col      # New coordinates
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or 
                        grid[nr][nc] == "0"):        # Skip if out of bounds or water
                        continue
                    q.append((nr, nc))               # Add neighbor to queue
                    grid[nr][nc] = "0"               # Mark as visited immediately

        for r in range(rows):                        # Check every cell in grid
            for c in range(cols):
                if grid[r][c] == "1":                # Found unvisited land
                    bfs(r, c)                        # Explore entire island
                    islands += 1                     # Count this island
                    
        return islands
