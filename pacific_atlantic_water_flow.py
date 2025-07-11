#do reverse, like water coming from ocean to cell,if height is equal or greather then come
#make two hash sets for both sets where water comes from pacific and atlantic, and find common

#bruteforce: 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()                     # Cells reachable by each ocean

        def dfs(r, c, visit, prevHeight):           # DFS to find reachable cells
            if ((r, c) in visit or                  # Already visited
                r < 0 or c < 0 or                   # Out of bounds (top/left)
                r == ROWS or c == COLS or           # Out of bounds (bottom/right)
                heights[r][c] < prevHeight):        # Can't flow uphill
                return
            
            visit.add((r, c))                       # Mark as reachable
            # Explore all 4 directions
            dfs(r + 1, c, visit, heights[r][c])     # Down
            dfs(r - 1, c, visit, heights[r][c])     # Up
            dfs(r, c + 1, visit, heights[r][c])     # Right
            dfs(r, c - 1, visit, heights[r][c])     # Left

        # Start DFS from Pacific edges (top and left)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])           # Top edge
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])           # Left edge

        # Start DFS from Atlantic edges (bottom and right)
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom edge
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right edge

        # Find cells reachable by both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
