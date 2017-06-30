class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        rmax = 0
        tmax = 0
        index = 0
        length = len(s)
        for i in range(length):
            if s[i] in d and index <= d[s[i]]:
                index = d[s[i]] + 1
                rmax = max(rmax, tmax)
            else:
                tmax = i - index + 1
            d[s[i]] = i
        rmax = max(rmax, tmax)
        return rmax
                
               