# Process the entire persons list by calculating a list of current leader after every vote
# Perform bisect (find index where element would go if in sorted order, or the right most existence of element)
#   and use found index to search for leader
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        currentLeader = None
        self.leaderList = []
        voteCounter = defaultdict(lambda: 0)
        for person in persons:
            voteCounter[person] += 1
            if currentLeader == None:
                currentLeader = person
            if voteCounter[person] >= voteCounter[currentLeader]:
                currentLeader = person
            self.leaderList.append(currentLeader)
        assert len(self.leaderList) == len(times)


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = bis(self.times, t)
        return self.leaderList[idx]


def bis(l, val):
    high = len(l) - 1
    low = 0
    while high != low:
        mid = (high + low) // 2
        if l[mid] == val:
            return mid
        elif l[mid] < val:
            if low == mid:
                if l[low + 1] <= val:
                    low += 1
                else:
                    return low
            else:
                low = mid
        else: # val < l[mid]
            if mid != 0 and l[mid-1] < val:
                return mid - 1
            else:
                high = mid
    return high # or low, they are same
        


if __name__ == "__main__":
    print("=== 911_online_election_top_voted_candidate")
    topVotedCandidate = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
    assert topVotedCandidate.q(3) == 0
    assert topVotedCandidate.q(12) == 1
    assert topVotedCandidate.q(25) == 1
    assert topVotedCandidate.q(15) == 0
    assert topVotedCandidate.q(24) == 0
    assert topVotedCandidate.q(8) == 1
    print("=== done! ===")

