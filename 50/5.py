class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in xrange(len(s)):
            temp = ''
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                temp = s[l+1:r]
            if len(temp) > len(res):
                res = temp

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                temp = s[l+1:r]
            if len(temp) > len(res):
                res = temp

        return res