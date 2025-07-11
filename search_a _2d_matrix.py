'''
Brute Force Method
Scan every element in the 2D matrix row by row and column by column, 
comparing each to the target. Return True if any element matches the target, 
otherwise return False.

Time Complexity: O(m × n) (where m = number of rows, n = number of columns)

Space Complexity: O(1) (no extra space except variables)

def searchMatrix(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

'''
'''
Optimal Method (Binary Search on Virtual 1D Array)
Treat the 2D matrix as a single sorted 1D array (since each row's first element is 
greater than the previous row's last). Use binary search to efficiently find the target.

Time Complexity: O(log(m × n)) (binary search over all elements)

Space Complexity: O(1) (no extra space except variables)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ro, co = len(matrix), len(matrix[0])    # Get matrix dimensions
        l, r = 0, ro * co - 1                  # Treat as 1D array: left=0, right=last_index
        
        while l <= r:                          # Standard binary search
            m = l + (r - l) // 2               # Find middle index
            row, col = m // co, m % co         # Convert 1D index to 2D coordinates
            
            if target > matrix[row][col]:      # Target is larger
                l = m + 1                      # Search right half
            elif target < matrix[row][col]:    # Target is smaller
                r = m - 1                      # Search left half
            else:                              # Found target
                return True
                
        return False                           # Target not found

        