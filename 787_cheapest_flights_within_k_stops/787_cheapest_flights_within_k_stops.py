import math
import heapq

class Solution:
    # Kind of like k depth BFS, but with heap to take shortest edge first
    # Kind of like djikstras, but can have multiple dist entries in heap for single node
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # build adjacency list graph; (dest, cost)
        graph = [[] for x in range(n)]
        for flight in flights:
            source, destination, cost = flight
            graph[source].append((destination, cost))

        
        # default to not possible
        shortest_dist = math.inf
        # (distance, node, jumps_left)
        node_heap = [(0,src,K + 1)]
        # do BFS/djikstras
        while node_heap:
            node = heapq.heappop(node_heap)

            # if dst found, possible update shortest_dist
            if node[1] == dst:
                shortest_dist = node[0]
                break

            # if more hops allowed
            if node[2] > 0:
                for next_node in graph[node[1]]:
                    heapq.heappush(node_heap, (node[0] + next_node[1], next_node[0], node[2] - 1))

        if shortest_dist == math.inf:
            return -1
        return shortest_dist


if __name__ == "__main__":
    print("=== findCheapestPrice ===")

    res = Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
    print(res)
    assert res == 200

    res = Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
    print(res)
    assert res == 500

    print("=== done! ===")