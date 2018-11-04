class Solution:
    # candies even length, split into 2 equal groups
    # what is the most number unique candies possible in ONE of the 2 groups
    # just find num_unique candies and take the min(num_unique, len(candies)/2)
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total_uniques = len(set(candies))
        return min(total_uniques, int(len(candies) / 2))

if __name__ == "__main__":
    print("=== distributeCandies ===")

    candies = [1,1,2,2,3,3]
    result = Solution().distributeCandies(candies)
    print(result)
    assert result == 3

    candies = [1,1,2,3]
    result = Solution().distributeCandies(candies)
    print(result)
    assert result == 2

    print("=== done! ===")