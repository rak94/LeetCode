class ClimbStairs:
    def climbing(self, num: int) -> int:
        one, two = 1, 1
        for i in range(num - 1):
            temp = one
            one = one + two
            two = temp
        return one