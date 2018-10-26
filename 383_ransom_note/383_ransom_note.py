from collections import defaultdict

class Solution:
    def canConstruct(self, ransom_note, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = defaultdict(lambda : 0)
        for c in magazine:
            magazine_dict[c] += 1

        for c in ransom_note:
            if c not in magazine_dict or magazine_dict[c] < 1:
                return False
            magazine_dict[c] -= 1
        return True

if __name__ == "__main__":
    print("=== canConstruct ransomNote ===")

    s = Solution()

    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True

    print("=== done! ===")