# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # sort intervals by ending times
    # iterate through the sorted list and whenever interval overlaps with the adjacent, 
    #   remove the one with the larger end time (makes more room for subsequent)
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        sorted_intervals = sorted(intervals, key = lambda x: x.end)
        current = sorted_intervals[0]
        counter = 0
        for j in range(len(sorted_intervals)):
            if j == 0:
                continue

            if current.end > sorted_intervals[j].start:
                counter += 1
                continue
            else:
                current = sorted_intervals[j]
        return counter

if __name__ == "__main__":
    print("=== erase overlap intervals ===")

    intervals = [ Interval(1,2), Interval(2,3), Interval(3,4), Interval(1,3) ]
    result = Solution().eraseOverlapIntervals(intervals)
    print(result)
    assert result == 1

    intervals = [ Interval(1,2), Interval(1,2), Interval(1,2) ]
    result = Solution().eraseOverlapIntervals(intervals)
    print(result)
    assert result == 2

    intervals = [ Interval(1,2), Interval(2,3) ]
    result = Solution().eraseOverlapIntervals(intervals)
    print(result)
    assert result == 0

    print("=== done! ===")