class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp={};
        for i in range(len(nums)):
            if not target-nums[i] in tmp:
                tmp[nums[i]]=i;
            else:
                return [tmp[target-nums[i]],i]