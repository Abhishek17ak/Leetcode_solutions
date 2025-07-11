#instead of finding surrounded regings, find everything except unsurounded regions
#we first scan all borders to find unsurrounded and turn it to T, and when we go insdie,
# it is guranteed to be surrounded  
#first traversal: we turn border o to t
#second traversal: we turn bewteen o's to x
#third traversal: we turn t back to o 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):                          # DFS to mark unsurrounded 'O's
            if (r < 0 or c < 0 or r == ROWS or      # Out of bounds
                c == COLS or board[r][c] != "O"):   # Not an 'O'
                return
            board[r][c] = "T"                       # Mark as "temporarily safe"
            capture(r + 1, c)                       # Explore all 4 directions
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Phase 1: Mark all border-connected 'O's as safe
        for r in range(ROWS):
            if board[r][0] == "O":                  # Left border
                capture(r, 0)
            if board[r][COLS - 1] == "O":           # Right border
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":                  # Top border
                capture(0, c)
            if board[ROWS - 1][c] == "O":           # Bottom border
                capture(ROWS - 1, c)

        # Phase 2: Convert remaining 'O's to 'X' and restore 'T's to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":              # Surrounded 'O' → capture it
                    board[r][c] = "X"
                elif board[r][c] == "T":            # Safe 'O' → restore it
                    board[r][c] = "O"
