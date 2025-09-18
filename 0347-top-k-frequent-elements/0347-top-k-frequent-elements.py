#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmp={};
        final=[];
        for i in nums:
            if not i in tmp:
                tmp[i]=1;
            else:
                tmp[i]+=1;
        final_list=sorted(tmp.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            final.append(final_list[i][0]);
        return final;


# @lc code=end

