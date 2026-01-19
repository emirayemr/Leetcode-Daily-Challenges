class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])

        # prefix sums: pre[i+1][j+1] = sum of mat[0..i][0..j]
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

        def square_sum(r, c, k):
            # sum of submatrix with top-left (r,c) and size k
            r2 = r + k
            c2 = c + k
            return pre[r2][c2] - pre[r][c2] - pre[r2][c] + pre[r][c]

        def exists(k):
            # any kxk square with sum <= threshold?
            if k == 0:
                return True
            if k > m or k > n:
                return False
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if square_sum(i, j, k) <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if exists(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
