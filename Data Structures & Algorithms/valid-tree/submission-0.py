class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        hashmap = { i:[] for i in range(n)}
        for node, edge in edges:
            hashmap[node].append(edge)
            hashmap[edge].append(node)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for i in hashmap[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
            