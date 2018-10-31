class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # note, binary tree, not binary search tree
    # essentially use the max of the sublist as root and recurse
    # use pointers in each recursive call to prevent the need to splice and make copies of data in memory
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        print(nums)
        def construct(nums, i, j):
            # print("calling on i,j ", i, j)
            if i == j:
                return TreeNode(nums[i])

            split_index = nums.index(max(nums[i:j+1]))
            root = TreeNode(nums[split_index])
            if split_index != i:
                root.left = construct(nums, i, split_index - 1)
            if split_index != j:
                root.right = construct(nums, split_index + 1, j)
            return root

        return construct(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    print("=== constructMaximumBinaryTree ===")

    root = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
    assert root.val == 6
    assert root.left.val == 3
    assert root.left.left == None
    assert root.left.right.val == 2
    assert root.left.right.left == None
    assert root.left.right.right.val == 1
    assert root.left.right.right.left == None
    assert root.left.right.right.right == None
    assert root.right.val == 5
    assert root.right.right == None
    assert root.right.left.val == 0
    assert root.right.left.left == None
    assert root.right.left.right == None


    #   6
    #  /   \
    # 3     5
    #  \    / 
    #   2  0   
    #     \
    #      1

    print("=== done! ===")