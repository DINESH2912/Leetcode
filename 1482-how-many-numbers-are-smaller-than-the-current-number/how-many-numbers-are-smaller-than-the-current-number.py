class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        b=[]
        
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
                else:
                    pass
            b.append(count)

        return b



