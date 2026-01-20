class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for p in nums:
            # x | (x+1) is always odd, so even p is impossible (e.g., 2)
            if (p & 1) == 0:
                ans.append(-1)
                continue

            # k = number of trailing 1-bits in p
            k = 0
            while (p >> k) & 1:
                k += 1

            # minimal x occurs by taking the largest possible k
            # x = p - 2^(k-1)
            ans.append(p - (1 << (k - 1)))

        return ans
