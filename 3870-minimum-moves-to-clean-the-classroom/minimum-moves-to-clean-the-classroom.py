from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        full = (1 << k) - 1

        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque()
        q.append((sr, sc, energy, 0, 0))
        best[sr][sc][0] = energy

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                if ne <= best[nr][nc][nmask]:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, ne, nmask, moves + 1))

        return -1