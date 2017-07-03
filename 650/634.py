class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        X, Y = 1, 0
        for i in xrange(2, n+1):
            X, Y = Y, (i - 1) * (X + Y) % MOD
        return Y       