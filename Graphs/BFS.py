# Breadth First Search (BFS) implementation in Python
from collections import deque
from typing import List, Optional

class Solution:
    def bfs(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        result = []
        queue = deque([0])  # Start BFS from the first node (0)
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
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
    print("BFS traversal of the graph is:")
    print(solution.bfs(graph))
# Output: [0, 1, 2, 3, 4, 5]
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) for the visited set and queue