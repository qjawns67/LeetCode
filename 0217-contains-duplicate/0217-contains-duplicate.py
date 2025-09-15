#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp={};
        for i in nums:
            if not i in tmp:
                tmp[i]=i;
            else:
                return True;
        return False;
# @lc code=end

