class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0
        two = 1
        for _ in range(n):
            no_of_ways = one + two
            one = two
            two = no_of_ways
        return no_of_ways