class Solution:
    # DFS from each coordinate looking for increasing path, while utilizing DP
    # O(N * M), DFS will visit each coordinate once, bc DP saves revisiting node and no way to go backwards on path
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # given a coordinate, return whether or not it is a valid place in the matrix
        def in_matrix(i,j):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
                return True
        
        # given a coordinate, return all cardinal adjacent coordinates where the value is greater than the given coordinate's
        CARDINAL_DIRS = [[0,-1], [1,0], [0,1], [-1,0]]
        def get_next_increasing_spaces(i,j):
            increasing_spaces = []
            for c_dirs in CARDINAL_DIRS:
                poss_i, poss_j = i + c_dirs[0], j + c_dirs[1]
                if in_matrix(poss_i, poss_j):
                    if matrix[poss_i][poss_j] > matrix[i][j]:
                        increasing_spaces.append([poss_i, poss_j])
            return increasing_spaces

        # given a coordinate, does recursive DFS through increasing spaces to return the max path ending on the coordinate
        # also utilizes DP to prevent recomputation of coordinates
        dp_longest_path_from = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        def do_dp(i,j):
            # already visited
            if dp_longest_path_from[i][j] != 0:
                return dp_longest_path_from[i][j]

            # check all increasing directions
            max_len = 1
            for space in get_next_increasing_spaces(i,j):
                poss_len = 1 + do_dp(space[0], space[1])
                max_len = max(max_len, poss_len)
            dp_longest_path_from[i][j] = max_len
            return max_len

        # run DP DFS from each coordinate and track max
        longestLength = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longestLength = max(longestLength, do_dp(i,j))
        return longestLength




if __name__ == "__main__":
    print("=== longestIncreasingPath ===")

    s = Solution()
    
    nums = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ] 
    assert s.longestIncreasingPath(nums) == 4

    nums = [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ] 
    assert s.longestIncreasingPath(nums) == 4

    print("=== done! ===")