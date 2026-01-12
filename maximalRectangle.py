class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(h):
            stack = []
            best = 0
            for i in range(len(h) + 1):
                cur = 0 if i == len(h) else h[i]
                while stack and cur < h[stack[-1]]:
                    height = h[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    best = max(best, height * width)
                stack.append(i)
            return best

        for r in range(len(matrix)):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
