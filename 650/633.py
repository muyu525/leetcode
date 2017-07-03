class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        max_n = int(math.sqrt(c)) + 1
        for i in range(max_n):
            n = c - i * i
            if math.modf(math.sqrt(n))[0] == 0:
                return True
        return False