
class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        N = n + k - 1
        R = 2 * k

        fact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        numerator = fact[N]
        denominator = fact[R] * fact[N - R] % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD