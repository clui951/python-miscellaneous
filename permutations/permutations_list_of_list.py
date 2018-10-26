class Solution:
    # build entire list of permutations and return
    def perm_list_of_lists(self, lists):
        permutations = [[]]
        for ls in lists:
            new_permutations = []
            for elem in ls:
                for p in permutations:
                    new_permutations.append(p + [elem])
            permutations = new_permutations
        return permutations

    # build and print in place
    def print_perm_list_of_lists(self, lists):
        perm = [None for _ in  range(len(lists))]
        def build_perm(lists, idx):
            if idx == len(lists):
                print(perm)
                return

            for elem in lists[idx]:
                perm[idx] = elem
                build_perm(lists, idx + 1)

        build_perm(lists, 0)
        

def compare_equal_lists(l1, l2):
    assert len(l1) == len(l2)
    for a in l1:
        assert a in l2
    for b in l2:
        assert b in l1


if __name__ == "__main__":
    print("=== perm lists of lists ===")

    lists = [[1, 2, 3], [4], [5, 6]]
    expected = [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]]
    result = Solution().perm_list_of_lists(lists)
    print(result)
    compare_equal_lists(result, expected)

    print("--")

    Solution().print_perm_list_of_lists(lists)

    print("=== done! ===")