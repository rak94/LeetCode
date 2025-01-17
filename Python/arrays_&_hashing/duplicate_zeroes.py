from typing import List

def duplicate_zeroes(self, arr: List[int]) -> None:
    n = len(arr)
    zeroes = arr.count(0)
    i = n - 1
    j = n + zeroes - 1

    while i < j:
        if j < n:
            arr[j] = arr[i]

        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0

        i -= 1
        j -= 1