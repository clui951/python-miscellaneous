class Solution:
    # DP, for every element, either use or dont use
    # if use, take value plus max_sum ending on element 2 lower
    # if dont use, take max_sum ending on element 1 lower
    # max_sum ending on element is max of use and dont use
    def max_sum_non_adjacent_elements(self, nums):
        dp = [None for x in range(len(nums))]

        def max_sum(nums, i):
            if i == 0:
                dp[0] = max(0, nums[0])
                return dp[0]
            if i == 1:
                dp[1] = max(0, nums[0], nums[1])
                return dp[1]

            dp[i] = max(nums[i] + max_sum(nums, i - 2), max_sum(nums, i - 1)) 
            return dp[i]

        return max_sum(nums, len(nums) - 1)

if __name__ == "__main__":
    print("=== max_sum_non_adjacent_elements ===")

    assert Solution().max_sum_non_adjacent_elements([1, 0, 3, 9, 2]) == 10

    print("=== done! ===")