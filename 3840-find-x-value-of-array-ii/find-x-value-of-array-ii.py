class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        if k == 1:
            return [n - q[2] for q in queries]

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i, v in enumerate(nums):
            v %= k
            p = size + i
            prod[p] = v
            cnt[p][v] = 1

        def pull(p):
            left = p * 2
            right = left + 1

            prod[p] = (prod[left] * prod[right]) % k

            for r in range(k):
                cnt[p][r] = cnt[left][r]

            for r in range(k):
                cnt[p][(prod[left] * r) % k] += cnt[right][r]

        for p in range(size - 1, 0, -1):
            pull(p)

        def merge(p1, c1, p2, c2):
            p = (p1 * p2) % k
            c = c1[:]

            for r in range(k):
                c[(p1 * r) % k] += c2[r]

            return p, c

        result = []

        for index, value, start, x in queries:
            # Update
            pos = size + index
            value %= k

            prod[pos] = value
            cnt[pos] = [0] * k
            cnt[pos][value] = 1

            pos //= 2

            while pos:
                pull(pos)
                pos //= 2

            # Query [start, n-1]
            left = size + start
            right = size + n

            lp = 1
            lc = [0] * k

            rp = 1
            rc = [0] * k

            while left < right:
                if left & 1:
                    lp, lc = merge(lp, lc, prod[left], cnt[left])
                    left += 1

                if right & 1:
                    right -= 1
                    rp, rc = merge(prod[right], cnt[right], rp, rc)

                left //= 2
                right //= 2

            _, final_count = merge(lp, lc, rp, rc)

            result.append(final_count[x])

        return result