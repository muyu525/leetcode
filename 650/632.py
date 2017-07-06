class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ans = -1e9, 1e9
        for right in sorted(set(x for l in nums for x in l))[::-1]:
            for l in nums:
                while l and right < l[-1]:
                    l.pop()
                if not l:
                    return ans
            left = min(l[-1] for l in nums)
            if right - left <= ans[1] - ans[0]:
                ans = left, right
        return ans 


