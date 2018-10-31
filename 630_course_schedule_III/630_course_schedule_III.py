import heapq

class Solution:
    # first sort by deadline 
    # for every single class with increasing deadline, (lets call them the first k classes)
    #   we want to use all classes up to it to take as many classes up to the deadline
    #   add the kth class to heap, and then continually remove the largest class until under the deadline
    #   repeat for following classes; we will never prefer a longer class over a shorter one, so can DP it
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        heap = []
        running_length = 0
        for length, deadline in sorted(courses, key = lambda x: x[1]):
            running_length += length
            # heapq is a min-heap (returns smallest elem), so put in negatives
            heapq.heappush(heap, -length)
            while running_length > deadline:
                # lengths in heap are negative
                running_length += heapq.heappop(heap)

        return len(heap)

if __name__ == "__main__":
    print("=== scheduleCourse ===")

    # (num days, day deadline)
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    result = Solution().scheduleCourse(courses)
    print(result)
    assert result == 3

    courses = [[5,5],[4,6],[2,6]]
    result = Solution().scheduleCourse(courses)
    print(result)
    assert result == 2

    print("=== done! ===")