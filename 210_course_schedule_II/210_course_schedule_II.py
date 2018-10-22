class Solution(object):
    # for prerequisite [1,0], 1 depends on 0 and must be completed after 0
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if len(prerequisites) == 0:
            return list(range(numCourses))

        # build dependency graph
        # each parent has list of dependencies that must be completed before it can
        dependency_graph = [[] for x in range(numCourses)]
        def build_graph(prerequisites):
            for depender, prereq in prerequisites:
                dependency_graph[depender].append(prereq)
        
        job_order = []
        visited = [0 for x in range(numCourses)]
        # builds up job_order list, but also returns True/False for success or not (cycle detection)
        # DFS while tracking visited to determine if to be visited/currently visiting/visited ; 0/-1/1
        # For every job, recursively visit each dependency
        # Once all dependencies visited, visit self and append to job_order
        def dfs_find_order(currJob):
            if visited[currJob] == -1:
                return False
            if visited[currJob] == 1:
                return True

            visited[currJob] = -1
            for prereq in dependency_graph[currJob]:
                if dfs_find_order(prereq) == False:
                    return False

            job_order.append(currJob)
            visited[currJob] = 1
            return True

        # build graph & processes every job
        # if cycle detected at any time, return empty list
        build_graph(prerequisites)
        for job in range(numCourses):
            if dfs_find_order(job) == False:
                return []
        return job_order


if __name__ == "__main__":
    print("=== findOrder ===")

    order = Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) 
    assert order in [[0,1,2,3], [0,2,1,3]]

    print("=== done! ===")