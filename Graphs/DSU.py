class DSU:
    def __init__(self, n):
        # Initializes n+1 nodes (assuming 1-based indexing)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, u):
        """
        Finds the representative (root parent) of the set that u belongs to.
        Applies path compression for optimization.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union_by_size(self, u, v):
        """
        Unites the sets that contain u and v using union by size.
        Returns True if union was successful (i.e., u and v were in different sets),
        and False if u and v were already in the same set.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Already in the same set

        # Attach smaller set under larger set
        if self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]

        return True
    def union_by_rank(self, u, v):
        """
        Unites the sets that contain u and v using union by rank.
        Returns True if union was successful (i.e., u and v were in different sets),
        and False if u and v were already in the same set.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Already in the same set

        # Union by rank
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True