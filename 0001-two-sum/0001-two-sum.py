class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp={};
        for i in range(len(nums)):
            if target-nums[i] in tmp:
                return [tmp[target-nums[i]],i];
            else:
                tmp[nums[i]]=i;