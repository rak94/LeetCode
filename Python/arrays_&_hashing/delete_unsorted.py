from typing import List

def delete_unsorted(self, strs: List[str]) -> int:
    unsorted_count = 0
    
    for col in range(len(strs[0])):
        for row in range(1, len(strs)):
            if strs[row][col] < strs[row - 1][col]:
                unsorted_count += 1
                break
    
    return unsorted_count