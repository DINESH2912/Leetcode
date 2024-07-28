class Solution(object):
    def getConcatenation(self, nums):
        length=len(nums)
        nums.extend([0] * length) 
        # nums.extend is used to extend the array.
        count=0
        for i in range(length,2*length,1):
            nums[i]=nums[count]
            count+=1
        return nums

        