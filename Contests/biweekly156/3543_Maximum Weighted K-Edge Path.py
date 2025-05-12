# Build the adjacency list from the list of directed weighted edges:
# adj[u] will store (v, w) pairs meaning there's an edge u → v with weight w.

# Initialize a DP table:
# Use dist[node][num_edges] = set of total weights to store all path weights that reach node using exactly num_edges.

# Base case:
# For all nodes i, add 0 to dist[i][0] — meaning we can start at any node with 0 edges and 0 weight.

# Iterate for each edge count edge from 0 to k-1:
# For each node u, for each weight curr in dist[u][edge],
# try extending the path to all neighbors nbr via edge weight wt.

# Update the neighbor's DP set:
# If curr + wt < t, add the new weight to dist[nbr][edge + 1].

# After building all paths, check every node i and find the maximum weight in dist[i][k] that is still < t.

# Return the maximum such weight, or -1 if no such path exists.

from collections import defaultdict, deque
from typing import List

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:

        adj = defaultdict(list)
        for u,v, w in edges:
            adj[u].append((v,w))
       
        dist = [defaultdict(set) for _ in range(n)]
        for i in range(n):
            dist[i][0].add(0)

        
        for edge in range(k):
            for u in range(n):
                for curr in dist[u][edge]:
                    for nbr, wt in adj[u]:
                        new_wt = curr+wt
                        if(new_wt<t):
                            dist[nbr][edge+1].add(new_wt)

        max_wt = -1
        for i in range(n):
            for wts in dist[i][k]:
                max_wt = max(max_wt, wts)
        return max_wt