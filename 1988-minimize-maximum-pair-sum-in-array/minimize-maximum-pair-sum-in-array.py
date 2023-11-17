class Solution(object):
    def minPairSum(self, nums):
        max_num=0
        x=sorted(nums)
        a=0
        b=len(nums)-1
        while(a<b):
            if x[a]+x[b]>max_num:
                max_num=x[a]+x[b]
            else:
                a=a+1
                b=b-1

        return max_num