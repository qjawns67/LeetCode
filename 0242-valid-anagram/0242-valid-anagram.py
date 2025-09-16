#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr_s=list(s);
        arr_s.sort();
        arr_t=list(t);
        arr_t.sort();
        if len(arr_s)!=len(arr_t):
            return False;
        else:
            for i in range(len(arr_t)):
                if arr_s[i]!=arr_t[i]:
                    return False;
        return True;
# @lc code=end

