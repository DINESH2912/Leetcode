class Solution(object):
    def checkIfExist(self, arr):
        arr=sorted(arr)
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if (arr[i]*2==arr[j]) or (arr[j]*2==arr[i]):
                    return True
                else:
                    pass
        return False
        