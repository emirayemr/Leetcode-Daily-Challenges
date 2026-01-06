# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # not needed for LeetCode constraints, but safe

        q = deque([root])
        level = 0
        best_level = 1
        best_sum = float("-inf")

        while q:
            level += 1
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # smallest level with maximal sum: update only on strictly greater
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level

        return best_level
