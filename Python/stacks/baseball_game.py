# create empty stack
# check for the values, assign conditions
# perform operation based on the conditions
from typing import List

class BaseballGame():
    def baseball_game(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                stack.append(2 * stack[-1])
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
        
        return sum(stack)