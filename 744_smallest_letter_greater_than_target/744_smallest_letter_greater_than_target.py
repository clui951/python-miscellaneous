class Solution:
    # essentially do a bisect of letters using target
    # but no matter if found or not, take one element greater
    # use wrap around on last element
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if len(letters) == 0:
            return ""
        elif len(letters) == 1:
            return letters[0]

        low = 0
        high = len(letters) - 1
        mid = None
        # after this loop, mid+1 is the element we want
        while low < high:
            mid = (low + high) // 2
            # low/high next to each other case
            if mid == low:
                if letters[mid] == target:
                    break
                elif letters[mid+1] <= target:
                    mid += 1
                    break
                else:
                    break
            # continue searching case
            else:
                if letters[mid] == target:
                    break
                elif letters[mid] > target:
                    high = mid
                else:
                    low = mid

        # emulate bisect_right; picks element on right of all occurence
        mid2 = mid
        while True:
            mid2_plus1 = mid2 + 1 if mid2 < len(letters) - 1 else 0
            if letters[mid2_plus1] == target:
                mid2 = mid2_plus1
                # check wrapped around, all same elements
                if mid2 == mid:
                    return target
            else:
                # target is not repeated following mid
                break

        # wrap around case
        if mid2 == len(letters) - 1:
            return letters[0]
        # below lowest element case
        elif mid2 == 0 and target < letters[0]:
            return letters[0]
        else:
            return letters[mid2 + 1]
        

if __name__ == "__main__":
    print("=== nextGreatestLetter ===")
    s = Solution()
    letters = ["c", "f", "j"]

    target = "a"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "c"

    target = "c"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "f"

    target = "d"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "f"

    target = "g"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "j"

    target = "j"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "c"

    target = "k"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "c"


    letters = ["e","e","e","e","e","e","n","n","n","n"]
    target = "e"
    result = s.nextGreatestLetter(letters, target)
    print(result)
    assert result == "n"

    print("=== done! ===")