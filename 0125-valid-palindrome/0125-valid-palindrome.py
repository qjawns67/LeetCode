#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower();
        left=0;
        right=len(s)-1;
        while left<right:
            if s[left].isalnum()==False:
                left+=1;
                continue;
            if s[right].isalnum()==False:
                right-=1;
                continue;
            if s[left]==s[right]:
                left+=1;
                right-=1;
            else:
                return False;
        return True;
        
# @lc code=end

