class Solution(object):
    def maximumWealth(self, accounts):
        max=0
        for i in range(len(accounts)):
            if sum(accounts[i])>max:
                max=sum(accounts[i])
            else:
                pass
        return max