# Depth-First Search (DFS) implementation in Python
from typing import List, Optional

class Solution:
    def dfs(self, graph: List[List[int]], start: int, visited: set) -> List[int]:
        visited.add(start)
        result = [start]
        for neighbor in graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(graph, neighbor, visited))
        return result
# Example usage 
if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 3, 4],
        [0, 5],
        [1],
        [1],
        [2]
    ]
    solution = Solution()
    visited = set()
    print("DFS traversal of the graph is:")
    print(solution.dfs(graph, 0, visited))
# Output: [0, 1, 3, 4, 2, 5]
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) for the visited set used in the traversal
# Note: The order of traversal may vary depending on the order of neighbors in the adjacency list.
# The DFS implementation uses recursion to explore each node and its neighbors.