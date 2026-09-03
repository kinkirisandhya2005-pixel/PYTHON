class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_odd = float('inf')
        min_even = float('inf')
        has_odd = False
        has_even = False
        
        for x in nums1:
            if x % 2 == 1:
                has_odd = True
                if x < min_odd:
                    min_odd = x
            else:
                has_even = True
                if x < min_even:
                    min_even = x
        if not has_odd or not has_even:
            return True
        return min_odd < min_even