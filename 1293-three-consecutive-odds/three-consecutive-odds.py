class Solution(object):
    def threeConsecutiveOdds(self, arr):
        counts=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                counts+=1
                if counts==3:
                    return True
            else:
                counts=0
        return False
        