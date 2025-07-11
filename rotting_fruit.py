from collections import deque

class Solution:
    def orangesRotting(self,grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Initialize the queue with all rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1  # count fresh fruits

        # If no fresh fruits, we're done
        if fresh == 0:
            return 0

        minutes = -1
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Step 2: BFS to rot adjacent fruits
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # rot the fruit
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1  # after processing each level

    # If any fresh fruits are left, return -1
        return minutes if fresh == 0 else -1
