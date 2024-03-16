class Solution(object):
    def sumCounts(self, nums):
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                ans.append(len(set(nums[i:j]))**2)
        return sum(ans)


        