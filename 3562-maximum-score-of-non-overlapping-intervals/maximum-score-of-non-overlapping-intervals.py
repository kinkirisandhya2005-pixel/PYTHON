
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[1]
        )

        n = len(arr)
        ends = [x[1] for x in arr]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            p = bisect_left(ends, l, 0, i - 1)

            for k in range(1, 5):
                best = dp[i - 1][k]

                score, indices = dp[p][k - 1]
                candidate = (
                    score + w,
                    tuple(sorted(indices + (idx,)))
                )

                if candidate[0] > best[0] or (
                    candidate[0] == best[0] and
                    candidate[1] < best[1]
                ):
                    best = candidate

                dp[i][k] = best

        return list(dp[n][4][1])