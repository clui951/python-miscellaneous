class Solution:
        
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # range + 1 for when no chars left
        self.memo = [[None for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        return self.minimumDeleteSumMemo(s1, s2, 0, 0)
            
    def minimumDeleteSumMemo(self, s1, s2, i, j):
        if self.memo[i][j]:
            return self.memo[i][j]
        
        # base cases
        if i == len(s1) and j == len(s2):
            return 0
        if i == len(s1):
            val = sum([ord(c) for c in s2[j:]])
            self.memo[i][j] = val
            return val
        if j == len(s2):
            val = sum([ord(c) for c in s1[i:]])
            self.memo[i][j] = val
            return val
        
        # if same, remove both free of charge
        # if different, take min of removing each
        s1_char = s1[i]
        s2_char = s2[j]
        if s1_char == s2_char:
            return self.minimumDeleteSumMemo(s1, s2, i+1, j+1)
        else:
            val1 = ord(s1_char) + self.minimumDeleteSumMemo(s1, s2, i+1, j)
            val2 = ord(s2_char) + self.minimumDeleteSumMemo(s1, s2, i, j+1)
            val = min(val1, val2)
            self.memo[i][j] = val
            return val

if __name__ == "__main__":
	print("=== minimumDeleteSum ===")
	S = Solution()
	assert S.minimumDeleteSum("sea", "eat") == 231
	print("=== done! ===")
