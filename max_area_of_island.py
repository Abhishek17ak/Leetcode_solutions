from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0                                  # Track maximum area found
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 4 directions

        def bfs(r, c):                               # Returns area of current island
            q = deque()
            grid[r][c] = 0                           # Mark as visited (0 instead of "0")
            q.append((r, c))
            area = 1                                 # Start with area = 1 for current cell
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or 
                        grid[nr][nc] == 0):          # Check for 0 (not "0")
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0                 # Mark as visited
                    area += 1                        # Increment area for each land cell
            
            return area                              # Return total area of this island

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:                  # Found unvisited land (1 not "1")
                    current_area = bfs(r, c)         # Get area of this island
                    max_area = max(max_area, current_area)  # Update maximum
                    
        return max_area
