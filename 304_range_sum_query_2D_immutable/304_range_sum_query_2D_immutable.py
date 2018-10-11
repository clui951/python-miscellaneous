class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # DP solution, calculate sum for all rectangles (i,j) relative to (0,0)
        # Use venn diagram, 'OR' logic 
        # dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        self.dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum1 = 0
                if i > 0:
                    sum1 = self.dp[i-1][j]
                
                sum2 = 0
                if j > 0:
                    sum2 = self.dp[i][j-1]
                
                sub = 0
                if i > 0 and j > 0:
                    sub = self.dp[i-1][j-1]

                self.dp[i][j] = matrix[i][j] + sum1 + sum2 - sub
        [print(x) for x in matrix]
        print("===")
        [print(x) for x in self.dp]

    # returns dp[i][j] if valid indices, else 0
    def get(self, i, j):
        if i >= 0 and i < len(self.dp) and j >= 0 and j < len(self.dp[0]):
            return self.dp[i][j]
        else:
            return 0

    # [ X X X X X
    #   5 X X 3 X
    #   X 1 X X X
    #   X X X X X
    #   4 X X 2 X ]

    # sumRegion(1,2) = dp(2) - dp(3) - dp(4) + dp(5)
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        val = self.get(row2,col2) - self.get(row1 - 1, col2) - self.get(row2, col1 - 1) + self.get(row1 - 1, col1 - 1)
        print(val)
        return val
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



if __name__ == "__main__":
    print("=== range sum 2D immutable === ")
    
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    n = NumMatrix(matrix)
    assert n.sumRegion(2, 1, 4, 3) == 8
    assert n.sumRegion(1, 1, 2, 2) == 11
    assert n.sumRegion(1, 2, 2, 4) == 12

    print("=== done! ===")