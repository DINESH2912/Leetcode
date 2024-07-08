class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        m=x[::-1]
        if x==m:
            return True
        else:
            return False
        