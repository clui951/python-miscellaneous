class Solution(object):
    # dp starting from first to last element
    # let dp[i] be the maxSubArray ending on element i
    # dp[i] is just the max of just element nums[i] or nums[i] + maxSubArray ending at i-1
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for x in range(len(nums))]
        currMax = 0
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
                currMax = nums[0]
            else:
                dp[i] = max(nums[i] + dp[i-1], nums[i])
                if dp[i] > currMax:
                    currMax = dp[i]
        return currMax


if __name__ == "__main__":
    print("=== maxSubArray ===")

    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = s.maxSubArray(nums)
    print(res)
    assert res == 6

    print("=== done! ===")