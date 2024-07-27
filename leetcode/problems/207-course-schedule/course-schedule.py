class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        map = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            map[i[0]].append(i[1])

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if map[node] == []:
                return True
            
            visited.add(node)
            for i in map[node]:
                if not dfs(i):
                    return False
            
            visited.remove(node)
            map[node] = []
            return True
        
        for i in range(numCourses):
            if not map[i] == [] and not dfs(i):
                return False
        
        return True