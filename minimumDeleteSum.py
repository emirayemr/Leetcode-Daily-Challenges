class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)

        # dp[j] = min delete sum to make s1[:i] and s2[:j] equal (rolling 1D)
        dp = [0] * (n + 1)

        # Base: s1 is empty, delete all from s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            prev_diag = dp[0]          # dp[i-1][0]
            dp[0] += ord(s1[i - 1])    # dp[i][0]: delete all from s1[:i]

            for j in range(1, n + 1):
                temp = dp[j]  # store old dp[i-1][j] before overwrite

                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev_diag  # dp[i-1][j-1]
                else:
                    dp[j] = min(
                        dp[j] + ord(s1[i - 1]),      # delete s1[i-1]
                        dp[j - 1] + ord(s2[j - 1])   # delete s2[j-1]
                    )

                prev_diag = temp

        return dp[n]
