#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map={};
        for i in range(len(strs)):
            sorted_str="".join(sorted(strs[i]));
            if not sorted_str in map:
                tmp=[strs[i]];
                map[sorted_str]=tmp;
            else:
                map[sorted_str].append(strs[i]);
        return map.values();

# @lc code=end

