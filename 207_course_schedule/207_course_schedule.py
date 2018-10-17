# build directed adjacency graph of prereq -> subseq
# DFS from every node to find cycle (if cycle, canFinish = false)
# have a map to track visited
#   0 if unvisited
#   -1 if visiting in current search path of DFS from a root; in current DFS stack
#   1 if visited by a previous DFS iteration

# O(V + E)
#   O(E) to build graph
#   O(V + E) to DFS directed graph
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        class_graph = [[] for x in range(numCourses)]

        for pre in prerequisites:
            class_graph[pre[1]].append(pre[0])

        # 0 unvisited, -1 currently visiting, 1 visited
        dfs_visit_status = [0 for x in range(numCourses)]

        def dfs_no_cycle(val):
            if dfs_visit_status[val] == 1:
                return True
            elif dfs_visit_status[val] == -1:
                return False
            else:
                dfs_visit_status[val] = -1

                for subseq in class_graph[val]:
                    if not dfs_no_cycle(subseq):
                        return False

                dfs_visit_status[val] = 1
                return True

        for x in range(numCourses):
            if not dfs_no_cycle(x):
                return False
        return True
            


# n courses, 0 to n-1
# some have prereqs, ex. to take course 0, first take 1: [0, 1]
if __name__ == "__main__":
    print("=== canFinish ===")

    s = Solution()
    assert s.canFinish(2, [[1,0]] ) == True
    assert s.canFinish(2 , [[1,0],[0,1]]) == False

    print("=== done! ===")