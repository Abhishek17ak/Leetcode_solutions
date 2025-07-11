'''
Brute Force Method
For each cell, scan its entire row, column, and 3x3 box to check for duplicates.

Time Complexity: O(n³) (for each cell, scan O(n) elements in row, column, and box, with n = 9)

Space Complexity: O(1) (no extra space except for counters)

def isValidSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            # Check row and column
            for k in range(9):
                if k != j and board[i][k] == board[i][j]:
                    return False
                if k != i and board[k][j] == board[i][j]:
                    return False
            # Check 3x3 box
            box_row = 3 * (i // 3)
            box_col = 3 * (j // 3)
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if (r != i or c != j) and board[r][c] == board[i][j]:
                        return False
    return True
'''
'''
Use hash sets to track seen digits for each row, column, and 3x3 box as you scan the board once.

Time Complexity: O(n²) (each cell checked once, with O(1) set operations)

Space Complexity: O(n²) (for hash sets, but with n = 9, it's effectively constant)
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)      # Track numbers in each column
        rows = collections.defaultdict(set)      # Track numbers in each row
        squares = collections.defaultdict(set)   # Track numbers in each 3x3 box

        for r in range(9):                       # Check every cell
            for c in range(9):
                if board[r][c] == ".":           # Skip empty cells
                    continue
                if (board[r][c] in rows[r] or    # Check row for duplicate
                    board[r][c] in cols[c] or    # Check column for duplicate
                    board[r][c] in squares[(r//3, c//3)]):  # Check 3x3 box for duplicate
                    return False                 # Found duplicate - invalid!
                
                # Add current number to tracking sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True                              # No duplicates found - valid!
#O(n^2),O(n^2)
