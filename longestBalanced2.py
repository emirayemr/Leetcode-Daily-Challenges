class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        if n == 0:
            return 0

        ans = 1

        # Case 1: only 1 distinct char => any run is balanced
        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                ans = max(ans, run)
                run = 1
        ans = max(ans, run)

        # Helper for Case 2: only two letters (x,y), third letter acts as a barrier
        def best_two(x, y):
            best = 0
            diff = 0
            first = {0: -1}  # diff -> earliest index within current segment
            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    # reset at barrier
                    diff = 0
                    first = {0: i}
                    continue
                if ch == x:
                    diff += 1
                else:  # ch == y
                    diff -= 1
                if diff in first:
                    best = max(best, i - first[diff])
                else:
                    first[diff] = i
            return best

        # Case 2: exactly 2 distinct chars with equal counts
        ans = max(ans, best_two('a', 'b'), best_two('a', 'c'), best_two('b', 'c'))

        # Case 3: a, b, c all present with equal counts
        a = b = c = 0
        first = {(0, 0): -1}  # (a-b, a-c) -> earliest index
        best3 = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (a - b, a - c)
            if key in first:
                best3 = max(best3, i - first[key])
            else:
                first[key] = i

        ans = max(ans, best3)
        return ans
