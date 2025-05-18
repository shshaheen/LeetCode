from collections import defaultdict
from heapq import heappush, heappop
from typing import List
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        portals = defaultdict(list)

        if matrix[0][0] == '#' or matrix[-1][-1] == '#':
            return -1
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j].isalpha():
                    portals[matrix[i][j]].append((i, j))

        q = []
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        heappush(q, (0, 0, 0))  
        min_moves = [[float('inf')]*m for _ in range(n)]
        min_moves[0][0] =0
        used_portals = set()
        
        while q:
            moves, r, c = heappop(q)

            if (r, c) == (n - 1, m - 1):
                return moves

            cell = matrix[r][c]

            if cell.isalpha() and cell not in used_portals:
                for pr, pc in portals[cell]:
                    if (pr, pc)!= (r,c):
                        heappush(q, (moves, pr, pc))  
                used_portals.add(cell)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc):
                    if matrix[nr][nc] != '#' and min_moves[nr][nc]>moves+1:
                        min_moves[nr][nc] = moves+1
                        heappush(q, (moves + 1, nr, nc))
        
        return -1