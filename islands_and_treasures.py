'''
Optimal Method (Multi-Source BFS)
Perform BFS from all treasure chests at once. This ensures every land cell is filled with the minimum distance to any treasure, and each cell is visited only once.


Time Complexity: O(m × n) (each cell is visited at most once)


Space Complexity: O(m × n) (for the queue and visited set)
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()                           # Track visited cells
        q = deque()                             # BFS queue


        def addCell(r, c):                      # Helper to add valid cells to queue
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1):
                return                          # Skip invalid/visited/wall cells
            visit.add((r, c))                   # Mark as visited
            q.append([r, c])                    # Add to BFS queue


        # Find all treasures and add them to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:             # Found a treasure
                    q.append([r, c])            # Add to queue
                    visit.add((r, c))           # Mark as visited


        dist = 0                                # Current distance from treasures
        while q:                                # BFS level by level
            for i in range(len(q)):             # Process all cells at current distance
                r, c = q.popleft()              # Get next cell
                grid[r][c] = dist               # Set distance to treasure
                # Add all 4 neighbors to next level
                addCell(r + 1, c)               # Down
                addCell(r - 1, c)               # Up
                addCell(r, c + 1)               # Right
                addCell(r, c - 1)               # Left
            dist += 1                           # Increment distance for next level



