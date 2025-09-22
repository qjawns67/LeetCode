#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s,stack_t=[],[];
        for i in s:
            if not i=='#':
                stack_s.append(i);
            else:
                if not len(stack_s)==0:
                    stack_s.pop();
        
        for i in t:
            if not i=='#':
                stack_t.append(i);
            else:
                if not len(stack_t)==0:
                    stack_t.pop();
        
        if stack_s==stack_t:
            return True;
        else:
            return False;
# @lc code=end

