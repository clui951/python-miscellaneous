class Solution(object):
    # perform a twist on binary search
    # First two cases are the same (if low == mid / if target == nums[mid])
    # Next, we can figure out which side of the split is sorted (does not contain the rotation)
    #   Compare the mid against low/high, segments are sorted if elems low < mid, mid < high, or both 
    #   Using the knowledge of which side is sorted, we can then determine if the target lies in the sorted or unsorted side of each case
    #   That will also tell us which side to continue binary searching
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        low = 0
        high = len(nums) - 1
        while low != high:
            mid = (low + high) // 2
            if low == mid:
                if nums[low] == target:
                    return low
                else:
                    low += 1
                    continue
            if nums[mid] == target:
                return mid
            else:
                if nums[low] < nums[mid] < nums[high]:
                    # this whole segment is sorted
                    if target < nums[mid]:
                        high = mid
                    else:
                        low = mid
                elif nums[low] < nums[mid]:
                    # low segment sorted
                    if nums[low] <= target < nums[mid]:
                        high = mid
                    else:
                        low = mid
                else:
                    # high segment sorted
                    if nums[mid] < target <= nums[high]:
                        low = mid
                    else:
                        high = mid

        # low == high
        if nums[low] == target:
            return low
        else:
            return -1

if __name__ == "__main__":
    print("=== search in rotated array ===")

    nums = [4,5,6,7,0,1,2]
    target = 0
    assert Solution().search(nums, target) == 4

    nums = [4,5,6,7,0,1,2]
    target = 3
    assert Solution().search(nums, target) == -1

    nums = [1,3,5]
    target = 5
    res = Solution().search(nums, target) 
    print(res, "== 2")
    assert res == 2

    nums = [3,5,1]
    target = 3
    res = Solution().search(nums, target) 
    print(res, "== 0")
    assert res == 0

    nums = [7,0,1,2,4,5,6]
    target = 0
    res = Solution().search(nums, target)
    print(res, "== 1")
    assert res == 1

    print("=== done! ===")