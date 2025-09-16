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
        if len(s)!=len(t):
            return False;
        else:
            tmp={};
            for i in s:
                if i in tmp:
                    tmp[i]+=1;
                else:
                    tmp[i]=1;
            for i in t:
                if i in tmp:
                    if tmp[i]>0:
                        tmp[i]-=1;
                    else:
                        return False; 
                else:
                    return False;
            return True;
# @lc code=end

