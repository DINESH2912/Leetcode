class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        ans = [[], []]
        for num in set1:
            if num not in set2:
                ans[0].append(num)
        for num in set2:
            if num not in set1:
                ans[1].append(num)
        return ans
