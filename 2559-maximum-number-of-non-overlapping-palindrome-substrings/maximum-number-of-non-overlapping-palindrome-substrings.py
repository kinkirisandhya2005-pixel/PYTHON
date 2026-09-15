
class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        pal = [bytearray(n) for _ in range(n)]

        for i in range(n):
            pal[i][i] = 1

            for j in range(i):
                if s[j] == s[i] and (i - j < 2 or pal[j + 1][i - 1]):
                    pal[j][i] = 1

        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = dp[i]

            for j in range(i - k + 1 + 1):
                if pal[j][i]:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)

        return dp[n]