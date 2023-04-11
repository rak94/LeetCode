from typing import List

class CombinationsSolution:
    def combination(self, num: int, k: int) -> List[int]:
        resArr = []

        def backtrack(start, comb):
            if len(comb) == k:
                resArr.append(comb.copy())
                return
            for i in range(start, num + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return resArr