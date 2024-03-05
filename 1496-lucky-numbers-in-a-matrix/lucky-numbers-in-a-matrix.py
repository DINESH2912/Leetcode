class Solution(object):
    def luckyNumbers(self,matrix):
        m, n = len(matrix), len(matrix[0])
        
        # Find the minimum element in each row
        row_min = [min(row) for row in matrix]
        
        # Find the maximum element in each column
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        
        # Find the intersection of row_min and col_max
        lucky_numbers = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers

        