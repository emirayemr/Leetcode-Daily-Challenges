class Solution(object):
    def sumFourDivisors(self, nums):
        total = 0

        for n in nums:
            if n < 6:   # 1..5 için 4 bölen olamaz
                continue

            div_sum = 1 + n
            div_count = 2  # 1 ve n

            r = int(n ** 0.5)
            for d in range(2, r + 1):
                if n % d == 0:
                    q = n // d
                    if q == d:
                        div_count += 1
                        div_sum += d
                    else:
                        div_count += 2
                        div_sum += d + q

                    if div_count > 4:
                        break

            if div_count == 4:
                total += div_sum

        return total
