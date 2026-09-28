class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in d:
                return [i, d[remainder]] 
            d[nums[i]] = i