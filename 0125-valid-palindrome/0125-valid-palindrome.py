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
        s=s.replace(' ','');

        new=[];
        for i in range(len(s)):
            if s[i].isalnum():
                new.append(s[i]);    

        if len(new)==0:
            return True;
        
        for i in range(len(new)/2):
            if new[i]!=new[len(new)-1-i]:
                return False;

        return True;

        
# @lc code=end

