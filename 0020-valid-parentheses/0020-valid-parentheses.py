#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[];
        tmp={']':'[','}':'{',')':'('};
        arr=list(s);
        for i in arr:
            if i=='[' or i=='{' or i=='(':
                stack.append(i);
            else:
                if len(stack)==0:
                    return False;
                else:
                    if stack.pop()!=tmp[i]:
                        return False;
        if len(stack)==0:
            return True;
        else:
            return False;         
# @lc code=end