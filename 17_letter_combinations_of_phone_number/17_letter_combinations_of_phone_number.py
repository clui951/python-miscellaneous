class Solution:
    letter_mappings =  {"2" : ["a", "b", "c"],
                        "3" : ["d", "e", "f"],
                        "4" : ["g", "h", "i"],
                        "5" : ["j", "k", "l"],
                        "6" : ["m", "n", "o"],
                        "7" : ["p", "q", "r", "s"],
                        "8" : ["t", "u", "v"],
                        "9" : ["w", "x", "y", "z"]}
    
    # calls recursive helper that yields (generators) combinations of letters starting from specified index to the end
    # space is O(N) where N is the length of digits, because we just need to track N generators
    # time is O(N) also, because for every index, we only call the helper once, and yield O(1), 3 or 4, elements per call
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        combinations = set()
        for combo in self.letterCombinationsHelper(digits, 0):
            combinations.add(combo)
        return list(combinations)

    def letterCombinationsHelper(self, digits, index):
        if index == len(digits):
            yield ""
            return
        
        d = digits[index]
        for combo in self.letterCombinationsHelper(digits, index + 1):
            for c in Solution.letter_mappings[d]:
                yield c + combo

if __name__ == "__main__":
    print("=== letterCombinations ===")

    s = Solution()
    actual = set(s.letterCombinations("23"))
    # print(actual)
    expected = set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    assert actual == expected

    print("=== done! ===")