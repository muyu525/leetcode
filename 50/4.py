class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = nums1, nums2
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 < len2:
            n1, n2 = nums2, nums1
            len1, len2 = len2, len1
        
        for item in n2:
            n1.append(item)
        n1.sort()
        median = 0
        length = len1 + len2
        if length%2 == 0:
            i = length/2
            median = (n1[i] + n1[i-1]) / 2.0
        else:
            i = int(length/2)
            median = n1[i]
        return median