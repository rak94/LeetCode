import re
from typing import List

class CourseScheduleTwo:
    def schedule(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c): False
            return []

        return output