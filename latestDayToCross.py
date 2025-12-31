from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """

        def can_cross(day):
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            visited = [[False] * col for _ in range(row)]

            # start from any land cell in top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        lo, hi = 0, row * col  # day in [0..R*C]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_cross(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
