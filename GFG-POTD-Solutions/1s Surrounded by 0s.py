from collections import deque

class Solution:
    def cntOnes(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        q = deque()
        
        # Push all boundary 1s
        for i in range(n):
            for j in [0, m - 1]:
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        
        for j in range(m):
            for i in [0, n - 1]:
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Remove all reachable boundary-connected 1s
        while q:
            x, y = q.popleft()
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        
        # Count remaining 1s
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        
        return count