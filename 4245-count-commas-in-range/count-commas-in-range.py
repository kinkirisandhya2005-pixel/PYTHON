class Solution(object):
    def countCommas(self, n):
        total = 0
        
        for i in range(1, n + 1):
            total += (len(str(i)) - 1) // 3
        
        return total