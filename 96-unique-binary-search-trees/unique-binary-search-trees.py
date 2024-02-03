class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        # Create an array to store previously computed results
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        return self.calculateNumTrees(n, dp)
    
    def calculateNumTrees(self, n: int, dp: List[int]) -> int:
        if dp[n] != 0:
            return dp[n]
        
        ans = 0
        for i in range(1, n + 1):
            ans += self.calculateNumTrees(i - 1, dp) * self.calculateNumTrees(n - i, dp)
        
        dp[n] = ans
        return ans
