class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        nums.sort()
        ans = float('inf')

        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < ans:
                ans = diff

        return ans
