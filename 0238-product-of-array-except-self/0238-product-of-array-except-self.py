#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[];
        for i in range(len(nums)):
            if i==0:
                answer.append(1);
            else:
                answer.append(nums[i-1]*answer[i-1]);
        right_num=1;
        for i in range(len(nums)):
            if i==0:
                right_num*=nums[len(nums)-i-1];
            else:
                answer[len(nums)-i-1]*=right_num;
                right_num*=nums[len(nums)-i-1];
        return answer;
# @lc code=end

