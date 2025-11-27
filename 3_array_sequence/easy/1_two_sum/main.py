class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, n in enumerate(nums):
            if target - n in index:
                return [index.get(target-n), i]
            index[n] = i
            
