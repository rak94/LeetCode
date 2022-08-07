from typing import List

class DailyTempSolution:
    def daily_temp(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        answer = [] # stores key value pair of index and temperature

        for i, temp in enumerate(temperatures):
            while answer and temp > answer[-1][0]:
                answerT, answerInd = answer.pop()
                res[answerInd] = (i - answerInd)
            answer.append([temp, i])
        return res