class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        temp = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if key in temp:
                result.append(temp.get(key))
                result.append(i)
                break
            temp[nums[i]] = i
        return result