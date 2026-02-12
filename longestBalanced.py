class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        if n == 0:
            return 0

        # prefix[c][i] = count of char c in s[:i]
        prefix = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s, 1):
            idx = ord(ch) - 97
            for c in range(26):
                prefix[c][i] = prefix[c][i - 1]
            prefix[idx][i] += 1

        ans = 0

        for l in range(n):
            # no need to try if even the longest remaining can't beat ans
            if n - l <= ans:
                break

            # only check substrings longer than current best
            for r in range(l + ans + 1, n + 1):
                mn = 10**9
                mx = 0
                distinct = 0

                for c in range(26):
                    cnt = prefix[c][r] - prefix[c][l]
                    if cnt:
                        distinct += 1
                        if cnt < mn:
                            mn = cnt
                        if cnt > mx:
                            mx = cnt

                if distinct > 0 and mn == mx:
                    ans = r - l

        return ans
