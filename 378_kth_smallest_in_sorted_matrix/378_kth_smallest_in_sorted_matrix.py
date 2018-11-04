import heapq

class Solution:
    # like other k smallest, use a heap
    # Use the heap to determine next path to search (almost like BFS/Djikstra's)
    # append on right/down (increasing) positions during visit of node
    # keep listed of visited positions, once visited k positions, we know it's kth smallest
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def in_matrix(pos):
            return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix)

        # (current_value, (x, y), k_left)
        search_heap = [(matrix[0][0], (0,0))]
        visited = set()
        while search_heap:
            lowest_val, pos = heapq.heappop(search_heap)
            if pos in visited:
                continue
            
            visited.add(pos)
            
            # found kth value
            if len(visited) == k:
                return lowest_val

            # search increasing directions, right or down
            right_pos = (pos[0], pos[1] + 1)
            if in_matrix(right_pos):
                heapq.heappush(search_heap, (matrix[right_pos[0]][right_pos[1]], right_pos))
            down_pos = (pos[0] + 1, pos[1])
            if in_matrix(down_pos):
                heapq.heappush(search_heap, (matrix[down_pos[0]][down_pos[1]], down_pos))

        return -1


if __name__ == "__main__":
    print("=== kthSmallest ===")

    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 8
    result = Solution().kthSmallest(matrix, k)
    print(result)
    assert(result) == 13

    print("=== done! ===")