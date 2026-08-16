class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        hashmap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if hashmap[crs] == []:
                return True
            visit.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            hashmap[crs] = []
            return True
        for crs in hashmap:
            if not dfs(crs):
                return False
        return True