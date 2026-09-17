class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        best = [INF] * n
        left = 0
        curr_sum = 0
        min_length = INF
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, best[left - 1] + length)

                min_length = min(min_length, length)

            best[right] = min(
                min_length,
                best[right - 1] if right > 0 else INF
            )

        return ans if ans != INF else -1