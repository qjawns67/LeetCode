#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #without converting Int to Str
        reverse_num=0;
        if x<0:
            return False;
        elif x==0:
            return True;
        else:
            if x%10==0:
                return False;
            else:
                while x>reverse_num:
                    reverse_num*=10;
                    reverse_num+=x%10;
                    x//=10;
        if x==reverse_num or x==reverse_num//10:
            return True;
        else:
            return False;
# @lc code=end

