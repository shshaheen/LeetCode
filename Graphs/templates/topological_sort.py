from collections import defaultdict, deque


def topological_sort(n, edges):
        graph = defaultdict(list)
        inorder = defaultdict(int)
        for v, u in edges:
            graph[u].append(v)
            inorder[v] += 1
            
        sources = deque([node for node in range(n) if inorder[node] == 0])
        order = []
        while sources:
            node = sources.popleft()
            order.append(node)
            for nei in graph[node]:
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    sources.append(nei)
        
        if len(order) == n:
            return order
        return []
