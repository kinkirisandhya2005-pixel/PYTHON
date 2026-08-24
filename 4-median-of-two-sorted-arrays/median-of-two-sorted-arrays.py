class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()

        length = len(merged)

        if length % 2 == 1:
            return float(merged[length // 2])

        return (merged[length // 2 - 1] + merged[length // 2]) / 2.0
        