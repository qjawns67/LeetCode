#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
import heapq;
# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmp={};
        for i in nums:
            if not i in tmp:
                tmp[i]=1;
            else:
                tmp[i]+=1;
        heap=[];
        for i in tmp.keys():
            heapq.heappush(heap,(tmp[i],i));
            if len(heap)>k:
                heapq.heappop(heap);
        
        return [heapq.heappop(heap)[1] for _ in range(k)];


# @lc code=end

