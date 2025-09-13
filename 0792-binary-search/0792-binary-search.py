#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index=0;
        right_index=len(nums)-1;
        current_index=(left_index+right_index)//2
        while left_index<=right_index:
            if nums[current_index]==target:
                return current_index;
            elif nums[current_index]<target:
                left_index=current_index+1;
                current_index=(left_index+right_index)//2;
                continue;
            else:
                right_index=current_index-1;
                current_index=(left_index+right_index)//2;
                continue;

        return -1;
# @lc code=end

