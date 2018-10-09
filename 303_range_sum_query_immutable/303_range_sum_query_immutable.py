class NumArray:

    # build out a list of sums from the left to each index
    # given i,j, take the sum of everything to j, minus the sume of everything to i - 1
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [None for i in range(len(nums))]
        
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            self.dp[i] = running_sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        assert i <= j
        assert i >= 0
        assert j < len(self.dp)

        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]


    # builds up a 2d, N^2 space matrix of all possible i,j pairs
    def __init__2(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [[None for j in range(len(nums))] for i in range(len(nums))]
        
        for i in range(len(nums)):
            running_sum = nums[i]
            self.dp[i][i] = running_sum
            for j in range(i + 1, len(nums)):
                self.dp[i][j] = self.dp[i][j-1] + nums[j]
        

    def sumRange2(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        assert i <= j
        assert i >= 0
        assert j < len(self.dp)
        return self.dp[i][j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    print("=== range sum immutable ===")
    nums = [-2, 0, 3, -5, 2, -1]
    n = NumArray(nums)
    assert n.sumRange(0,2) == 1
    assert n.sumRange(2, 5) == -1
    assert n.sumRange(0, 5) == -3
    print("=== done! ===")
