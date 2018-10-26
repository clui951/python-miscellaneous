class Solution:
    # build out list of permutations (like before) in memory 
    # at each step inserting a new character into every possible position of all permutations that exist so far
    # Unlike before, we need to detect / prevent duplicates
    # Whenever you're inserting into every position, when you see the same character you're inserting, stop
    #   if you insert after that value, it'll conflict with another permutation where it already has one after
    #       and they are inserting before
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = [[]]
        for n in nums:
            new_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    new_perm = p[:i] + [n] + p[i:]
                    new_permutations.append(new_perm)
                    if i < len(p) and p[i] == n:
                        break
            permutations = new_permutations
        return permutations

def compare_equal_lists(l1, l2):
    assert len(l1) == len(l2)
    for a in l1:
        assert a in l2
    for b in l2:
        assert b in l1

if __name__ == "__main__":
    print("=== permutations_unique ===")

    nums = [1,1,2]
    expected = [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    res = Solution().permuteUnique(nums)
    print(res)
    compare_equal_lists(res, expected)

    nums = [4,3,4,2,3]
    res = Solution().permuteUnique(nums)
    print(res)
    unique_res = [list(x) for x in set(tuple(x) for x in res)]
    assert len(res) == len(unique_res) ==  30 # 5! / (2! 2!)

    print("=== done! ===")

