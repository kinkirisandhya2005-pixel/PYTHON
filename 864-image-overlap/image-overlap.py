
class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        positions1 = []
        positions2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    positions1.append((i, j))
                if img2[i][j] == 1:
                    positions2.append((i, j))

        count = {}

        for r1, c1 in positions1:
            for r2, c2 in positions2:
                shift = (r1 - r2, c1 - c2)
                count[shift] = count.get(shift, 0) + 1

        return max(count.values()) if count else 0